from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import json
import logging
from dotenv import load_dotenv

from backend.llm_providers import LLMProviderFactory
from backend.rosa_expert import ROSAExpert
from backend.cli_executor import CLIExecutor

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__, static_folder='../frontend')
CORS(app)

# Initialize components
rosa_expert = ROSAExpert()
cli_executor = CLIExecutor()

# Global LLM provider (will be configured via settings)
current_provider = None

# Settings file path
# Settings file path
SETTINGS_FILE = '/tmp/settings.json'


def load_settings():
    """Load LLM provider settings from file"""
    try:
        if os.path.exists(SETTINGS_FILE):
            with open(SETTINGS_FILE, 'r') as f:
                return json.load(f)
    except Exception as e:
        logger.error(f"Error loading settings: {e}")
    
    # Check for Local LLM env var
    local_llm_endpoint = os.getenv('LOCAL_LLM_ENDPOINT')
    if local_llm_endpoint:
        return {
            'provider': 'local',
            'config': {
                'endpoint_url': local_llm_endpoint,
                'model': os.getenv('LOCAL_LLM_MODEL', 'mistral-7b-awq')
            }
        }

    # Check for Groq env var
    groq_api_key = os.getenv('GROQ_API_KEY')
    if groq_api_key:
        return {
            'provider': 'groq',
            'config': {
                'api_key': groq_api_key,
                'model': 'llama-3.1-8b-instant'
            }
        }

    # Default settings
    return {
        'provider': 'openai',
        'config': {
            'api_key': os.getenv('OPENAI_API_KEY', ''),
            'model': 'gpt-4'
        }
    }


def save_settings(settings):
    """Save LLM provider settings to file"""
    try:
        with open(SETTINGS_FILE, 'w') as f:
            json.dump(settings, f, indent=2)
        return True
    except Exception as e:
        logger.error(f"Error saving settings: {e}")
        return False


def initialize_provider():
    """Initialize LLM provider from saved settings"""
    global current_provider
    settings = load_settings()
    
    # Don't initialize if no API key or endpoint configured
    config = settings.get('config', {})
    if not config.get('api_key') and not config.get('endpoint_url'):
        logger.info("No API key or endpoint configured, skipping provider initialization")
        current_provider = None
        return
    
    try:
        current_provider = LLMProviderFactory.create_provider(
            settings['provider'],
            settings['config']
        )
        logger.info(f"Initialized {settings['provider']} provider successfully")
    except Exception as e:
        logger.warning(f"Failed to initialize provider during startup: {e}")
        logger.info("Provider will be created on-demand during first use")
        # Don't set current_provider to None - leave it as is
        # This allows the provider to be created fresh on each request


# Initialize provider on startup
initialize_provider()


@app.route('/')
def index():
    """Serve the main chat interface"""
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/<path:path>')
def serve_static(path):
    """Serve static files"""
    return send_from_directory(app.static_folder, path)


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    cli_versions = cli_executor.get_cli_versions()
    
    return jsonify({
        'status': 'healthy',
        'provider': current_provider.__class__.__name__ if current_provider else 'None',
        'cli_tools': cli_versions
    })


@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages with automatic command execution"""
    global current_provider
    
    # If no provider initialized, try to create it on-demand from saved settings
    if not current_provider:
        settings = load_settings()
        if settings.get('config', {}).get('api_key'):
            try:
                current_provider = LLMProviderFactory.create_provider(
                    settings['provider'],
                    settings['config']
                )
                logger.info(f"Created {settings['provider']} provider on-demand")
            except Exception as e:
                logger.error(f"Failed to create provider on-demand: {e}")
                return jsonify({
                    'error': f'Failed to initialize LLM provider: {str(e)}'
                }), 500
        else:
            return jsonify({
                'error': 'LLM provider not configured. Please configure in settings.'
            }), 400
    
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'Message is required'}), 400
        
        # Intelligent infrastructure state query detection
        # Map natural language questions to required verification commands
        message_lower = user_message.lower()
        
        # Infrastructure state query patterns and their required commands
        state_query_patterns = [
            # Cluster count/list queries
            ({'how many', 'cluster'}, 'rosa list clusters'),
            ({'list', 'cluster'}, 'rosa list clusters'),
            ({'what cluster', 'do i have'}, 'rosa list clusters'),
            ({'show', 'cluster'}, 'rosa list clusters'),
            ({'active cluster'}, 'rosa list clusters'),
            
            # Cluster status queries  
            ({'cluster', 'ready'}, None),  # Requires cluster name, handle specially
            ({'cluster', 'status'}, None),  # Requires cluster name, handle specially
            ({'deployment', 'complete'}, None),  # Requires cluster name, handle specially
            
            # Node queries
            ({'how many', 'node'}, 'oc get nodes'),
            ({'what node'}, 'oc get nodes'),
            ({'list', 'node'}, 'oc get nodes'),
            ({'show', 'node'}, 'oc get nodes'),
            
            # Version queries
            ({'what version'}, 'rosa list versions --output json'),
            ({'openshift version'}, 'oc version'),
            ({'rosa version'}, 'rosa version'),
            
            # Pod/workload queries
            ({'what', 'running'}, 'oc get pods -A'),
            ({'list', 'pod'}, 'oc get pods -A'),
            ({'show', 'pod'}, 'oc get pods -A'),
            
            # Region queries
            ({'what region'}, 'rosa list regions'),
            ({'available region'}, 'rosa list regions'),
        ]
        
        command_output = None
        executed_command = None
        
        # Check for infrastructure state queries
        for patterns, command in state_query_patterns:
            if all(pattern in message_lower for pattern in patterns):
                if command:
                    logger.info(f"Detected infrastructure state query, forcing command: {command}")
                    executed_command = command
                    result = cli_executor.execute(command)
                    command_output = result
                    break
        
        # Original command detection logic (for explicit commands in backticks/quotes)
        if not executed_command:
            # Check if user is explicitly asking to run a command
            command_keywords = ['run', 'execute', 'check', 'list', 'show', 'get', 'describe', 'verify']
            cli_tools = ['rosa', 'oc', 'aws', 'ocm']
            
            wants_execution = any(keyword in message_lower for keyword in command_keywords)
            mentions_cli = any(tool in message_lower for tool in cli_tools)
            
            # If it looks like a command request, try to detect and execute
            if wants_execution and mentions_cli:
                # Try to extract the actual command from the message
                import re
                # Look for quoted commands or code blocks
                cmd_patterns = [
                    r'`([^`]+)`',  # Backtick code
                    r'"([^"]+)"',  # Double quotes  
                    r'\'([^\']+)\'',  # Single quotes
                ]
                
                for pattern in cmd_patterns:
                    matches = re.findall(pattern, user_message)
                    for match in matches:
                        # Check if it's a valid CLI command
                        if cli_executor.validate_command(match):
                            logger.info(f"Detected command to execute: {match}")
                            executed_command = match
                            result = cli_executor.execute(match)
                            command_output = result
                            break
                    if executed_command:
                        break
        
        # Add user message to conversation
        rosa_expert.add_to_conversation('user', user_message)
        
        # If we executed a command, add the results to the conversation context
        if command_output:
            context_message = f"\n\n[SYSTEM - Command Executed: `{executed_command}`]\n"
            if command_output['success']:
                context_message += f"Output:\n```\n{command_output['output']}\n```"
            else:
                context_message += f"Error:\n```\n{command_output['error']}\n```\nExit code: {command_output['exit_code']}"
            
            # Add to conversation for context
            rosa_expert.add_to_conversation('system', context_message)
        
        # Get conversation messages with system prompt
        # Use provider-specific prompt (simplified for local endpoints)
        provider_class_name = current_provider.__class__.__name__
        messages = rosa_expert.get_conversation_messages_for_provider(provider_class_name)
        
        # Generate response from LLM
        response = current_provider.generate_response(messages)
        
        # Post-process response to detect and filter JSON command outputs
        import re
        import json as json_module
        
        # Check if response looks like a JSON command structure
        if re.search(r'\{\s*["\']cmd["\'\s]*:\s*\[', response):
            try:
                # Try to parse as JSON to confirm
                json_module.loads(response)
                # If it's valid JSON with 'cmd' key, replace with error message
                response = """I apologize, but I encountered an issue with my response format. Let me try again.

For ROSA CLI version, you can run:
```bash
rosa version
```

Please ask me again if you'd like me to check this for you."""
                logger.warning("Detected and filtered JSON command output from LLM")
            except:
                # Not valid JSON, keep original response
                pass
        
        # Add assistant response to conversation
        rosa_expert.add_to_conversation('assistant', response)
        
        # Prepare response with command execution info if applicable
        response_data = {
            'response': response,
            'success': True
        }
        
        if command_output:
            response_data['command_executed'] = {
                'command': executed_command,
                'success': command_output['success'],
                'output': command_output['output'],
                'error': command_output['error']
            }
        
        return jsonify(response_data)
        
    except Exception as e:
        logger.error(f"Chat error: {e}")
        return jsonify({
            'error': f'Error generating response: {str(e)}'
        }), 500


@app.route('/api/execute', methods=['POST'])
def execute_command():
    """Execute a CLI command"""
    try:
        data = request.json
        command = data.get('command', '')
        
        if not command:
            return jsonify({'error': 'Command is required'}), 400
        
        # Execute command
        result = cli_executor.execute(command)
        
        return jsonify(result)
        
    except Exception as e:
        logger.error(f"Command execution error: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/settings', methods=['GET'])
def get_settings():
    """Get current LLM provider settings"""
    settings = load_settings()
    
    # Mask API keys in response
    if 'config' in settings:
        # Mask api_key if present (for any provider)
        if 'api_key' in settings['config']:
            api_key = settings['config']['api_key']
            if api_key:
                settings['config']['api_key'] = api_key[:8] + '...' + api_key[-4:] if len(api_key) > 12 else '***'
    
    return jsonify(settings)


@app.route('/api/settings', methods=['POST'])
def update_settings():
    """Update LLM provider settings"""
    try:
        data = request.json
        provider = data.get('provider')
        config = data.get('config', {})
        
        if not provider:
            return jsonify({'error': 'Provider is required'}), 400
        
        # Validate provider
        settings = {
            'provider': provider,
            'config': config
        }
        
        # Only validate if test_connection is requested
        if data.get('test_connection', False):
            # Try to create provider to validate config
            try:
                test_provider = LLMProviderFactory.create_provider(provider, config)
                if not test_provider.validate_config():
                    return jsonify({
                        'success': False,
                        'error': 'Provider configuration validation failed'
                    }), 400
            except Exception as e:
                return jsonify({
                    'success': False,
                    'error': f'Invalid provider configuration: {str(e)}'
                }), 400
        
        # Save settings
        if save_settings(settings):
            # Reinitialize provider
            initialize_provider()
            
            return jsonify({
                'success': True,
                'message': 'Settings updated successfully'
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to save settings'
            }), 500
            
    except Exception as e:
        logger.error(f"Settings update error: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/conversation/clear', methods=['POST'])
def clear_conversation():
    """Clear conversation history"""
    rosa_expert.clear_conversation()
    return jsonify({'success': True})


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=os.getenv('DEBUG', 'False').lower() == 'true')
