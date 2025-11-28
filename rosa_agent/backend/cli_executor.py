import subprocess
import shlex
from typing import Dict, List, Tuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CLIExecutor:
    """Safe execution of whitelisted CLI commands"""
    
    # Whitelisted command prefixes
    ALLOWED_COMMANDS = [
        'rosa',
        'oc',
        'aws',
        'ocm'
    ]
    
    def __init__(self, timeout: int = 60):
        self.timeout = timeout
    
    def validate_command(self, command: str) -> bool:
        """Validate that command is in whitelist"""
        try:
            parts = shlex.split(command)
            if not parts:
                return False
            
            # Check if first part (command) is in whitelist
            base_command = parts[0]
            return any(base_command.startswith(allowed) for allowed in self.ALLOWED_COMMANDS)
        except Exception as e:
            logger.error(f"Command validation error: {e}")
            return False
    
    def execute(self, command: str) -> Dict[str, any]:
        """
        Execute a whitelisted command safely
        
        Returns:
            Dict with keys: success (bool), output (str), error (str), exit_code (int)
        """
        # Validate command
        if not self.validate_command(command):
            return {
                'success': False,
                'output': '',
                'error': f'Command not allowed. Only {", ".join(self.ALLOWED_COMMANDS)} commands are permitted.',
                'exit_code': -1
            }
        
        try:
            logger.info(f"Executing command: {command}")
            
            # Execute command
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=self.timeout
            )
            
            return {
                'success': result.returncode == 0,
                'output': result.stdout,
                'error': result.stderr,
                'exit_code': result.returncode
            }
            
        except subprocess.TimeoutExpired:
            logger.error(f"Command timeout: {command}")
            return {
                'success': False,
                'output': '',
                'error': f'Command timed out after {self.timeout} seconds',
                'exit_code': -1
            }
        except Exception as e:
            logger.error(f"Command execution error: {e}")
            return {
                'success': False,
                'output': '',
                'error': str(e),
                'exit_code': -1
            }
    
    def execute_multiple(self, commands: List[str]) -> List[Dict[str, any]]:
        """Execute multiple commands sequentially"""
        results = []
        for cmd in commands:
            result = self.execute(cmd)
            results.append(result)
            # Stop on first failure
            if not result['success']:
                break
        return results
    
    def get_cli_versions(self) -> Dict[str, str]:
        """Get versions of installed CLI tools"""
        version_commands = {
            'rosa': 'rosa version',
            'oc': 'oc version --client',
            'aws': 'aws --version',
            'ocm': 'ocm version'
        }
        
        versions = {}
        for tool, cmd in version_commands.items():
            result = self.execute(cmd)
            if result['success']:
                versions[tool] = result['output'].strip()
            else:
                versions[tool] = 'Not installed or error'
        
        return versions
