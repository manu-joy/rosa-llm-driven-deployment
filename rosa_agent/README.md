# 🚀 ROSA AI Agent

> An AI-powered chatbot specialized in Red Hat OpenShift Service on AWS (ROSA) cluster deployment and operations

## Overview

The ROSA AI Agent is a containerized intelligent assistant that provides expert guidance on deploying and managing ROSA clusters. Built with a modern web interface and pluggable LLM backend, it combines comprehensive ROSA knowledge with safe CLI command execution capabilities.

### Key Features

- 🤖 **Expert ROSA Knowledge**: Comprehensive understanding of ROSA HCP deployment, networking, and troubleshooting
- 💬 **Modern Chat Interface**: Sleek dark-themed UI with markdown and code highlighting support
- 🔌 **Multi-LLM Support**: Works with OpenAI (GPT-4), Anthropic (Claude), or local models (Ollama/vLLM)
- 🛠️ **CLI Integration**: Safe execution of ROSA, OC, AWS, and OCM commands within the container
- ⚙️ **Configurable**: Easy-to-use settings page for switching LLM providers
- 🐳 **Containerized**: Runs in Docker with all CLI tools pre-installed

## Quick Start

### Prerequisites

- Docker and Docker Compose installed
- LLM provider API key (OpenAI, Anthropic) OR local model endpoint
- (Optional) AWS credentials configured for ROSA operations

### 1. Clone and Navigate

```bash
cd rosa_agent
```

### 2. Configure Environment (Optional)

```bash
cp .env.example .env
# Edit .env with your LLM provider API keys (or configure via UI later)
```

### 3. Build and Run

```bash
docker-compose up -d
```

### 4. Access the Agent

Open your browser and navigate to:
```
http://localhost:5000
```

### 5. Configure LLM Provider

1. Click the **⚙️ Settings** button
2. Select your LLM provider (OpenAI, Anthropic, or Local)
3. Enter your API key or endpoint URL
4. Click **Test Connection** to verify
5. Click **Save Settings**
6. Return to chat and start asking questions!

## Usage Examples

### Ask About ROSA Deployment

```
User: How do I create a ROSA HCP cluster in Singapore?

Agent: To create a ROSA HCP cluster in Singapore (ap-southeast-1), follow these steps:

1. **Prerequisites Check:**
   - Ensure you're logged in: `rosa login`
   - Create account roles: `rosa create account-roles --mode auto --yes`
   - Set up billing account (HCP required)

2. **Create the Cluster:**
   ```bash
   rosa create cluster \
     --cluster-name my-singapore-cluster \
     --region ap-southeast-1 \
     --hosted-cp \
     --mode auto \
     --yes
   ```

3. **Monitor Progress:**
   ```bash
   rosa describe cluster --cluster my-singapore-cluster
   ```

The deployment typically takes 10-15 minutes for HCP clusters...
```

### Get CLI Command Help

```
User: What command shows available ROSA regions?

Agent: Use this command to list all ROSA regions:
```bash
rosa list regions
```

For HCP-specific regions only:
```bash
rosa list regions --hosted-cp
```
```

### Troubleshooting Assistance

```
User: I'm getting a billing account error when creating HCP cluster

Agent: This error occurs because ROSA HCP clusters require a billing account 
linked to your Red Hat account. Here's how to resolve it:

1. Navigate to: https://console.redhat.com/openshift/create/rosa/getstarted
2. Follow the billing account setup wizard
3. Link your AWS account
4. Verify with: `rosa whoami`

After setup, retry your cluster creation with the `--hosted-cp` flag.
```

## Architecture

```
┌─────────────────────────────────────────────────┐
│              ROSA AI Agent Container             │
│                                                  │
│  ┌──────────────────────────────────────────┐  │
│  │         Frontend (HTML/CSS/JS)            │  │
│  │  • Chat Interface                         │  │
│  │  • Settings Page                          │  │
│  │  • Markdown Rendering                     │  │
│  └──────────────────────────────────────────┘  │
│                       │                          │
│  ┌──────────────────────────────────────────┐  │
│  │      Flask API Backend (Python)           │  │
│  │  • /api/chat - Message handling           │  │
│  │  • /api/settings - LLM config             │  │
│  │  • /api/execute - CLI commands            │  │
│  │  • /api/health - Health check             │  │
│  └──────────────────────────────────────────┘  │
│            │              │              │       │
│  ┌─────────────┐ ┌──────────────┐ ┌──────────┐ │
│  │LLM Provider │ │ ROSA Expert  │ │   CLI    │ │
│  │  (OpenAI/   │ │  Knowledge   │ │ Executor │ │
│  │ Anthropic/  │ │     Base     │ │          │ │
│  │   Local)    │ └──────────────┘ └──────────┘ │
│  └─────────────┘                           │    │
│                                             │    │
│  ┌──────────────────────────────────────────┐  │
│  │         CLI Tools (Pre-installed)         │  │
│  │  • ROSA CLI  • OC CLI                     │  │
│  │  • AWS CLI   • OCM CLI                    │  │
│  └──────────────────────────────────────────┘  │
│                                                  │
│  [2GB Storage Volume]                           │
└─────────────────────────────────────────────────┘
```

## LLM Provider Configuration

### OpenAI

1. Get API key from https://platform.openai.com/api-keys
2. In Settings, select "OpenAI"
3. Enter API key
4. Choose model (GPT-4 recommended)
5. Save

### Anthropic Claude

1. Get API key from https://console.anthropic.com/
2. In Settings, select "Anthropic"
3. Enter API key
4. Choose model (Claude 3 Sonnet recommended for balance)
5. Save

### Local Models

For Ollama:
```bash
# Install and run Ollama on your host
ollama serve
ollama pull llama2

# In Settings:
Provider: Local Model
Endpoint: http://host.docker.internal:11434
Model: llama2
```

For vLLM or other OpenAI-compatible endpoints, use their API URL.

## CLI Command Execution

The agent can safely execute whitelisted CLI commands:
- ✅ `rosa` - ROSA CLI commands
- ✅ `oc` - OpenShift CLI commands
- ✅ `aws` - AWS CLI commands
- ✅ `ocm` - OCM CLI commands
- ❌ Other commands are blocked for security

Commands are executed within the container with a 60-second timeout.

## Container Details

### Installed CLI Tools

All tools are pre-installed in the container:
```bash
# Check versions
docker exec rosa-agent rosa version
docker exec rosa-agent oc version
docker exec rosa-agent aws --version
docker exec rosa-agent ocm version
```

### Storage Configuration

- **Volume**: 2GB allocated for CLI caches and logs
- **Location**: `./storage` directory (mounted to `/app/storage`)

### Resource Limits

- **Memory**: 2GB maximum, 512MB minimum reserved
- **Health Check**: Every 30 seconds via `/api/health`

## Development

### Project Structure

```
rosa_agent/
├── backend/
│   ├── app.py              # Flask API server
│   ├── llm_providers.py    # LLM provider abstraction
│   ├── rosa_expert.py      # ROSA knowledge base
│   ├── cli_executor.py     # CLI command executor
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── index.html          # Chat interface
│   ├── settings.html       # Settings page
│   ├── style.css           # Styling
│   ├── app.js              # Chat logic
│   └── settings.js         # Settings logic
├── Dockerfile              # Container definition
├── docker-compose.yml      # Orchestration config
└── README.md               # This file
```

### Running Locally (Development)

```bash
# Install Python dependencies
cd backend
pip install -r requirements.txt

# Run Flask development server
python app.py

# Access at http://localhost:5000
```

### Rebuilding Container

```bash
docker-compose down
docker-compose build
docker-compose up -d
```

## Knowledge Base

The agent's ROSA expertise is based on:
- ROSA Cluster creation agent instructions (from parent project)
- ROSA HCP deployment best practices
- Terraform module documentation
- CLI command references (ROSA, OC, AWS, OCM)

The system prompt is located in `backend/rosa_expert.py` and can be customized.

## Troubleshooting

### "LLM provider not configured" Error

- Go to Settings and configure your LLM provider
- Ensure API key is valid
- Click "Test Connection" to verify

### CLI Commands Not Working

- Ensure the container is running: `docker-compose ps`
- Check CLI tool availability: `docker exec rosa-agent rosa version`
- Verify command is whitelisted (rosa, oc, aws, ocm only)

### Container Won't Start

- Check Docker logs: `docker-compose logs rosa-agent`
- Verify port 5000 is not in use
- Ensure storage directory exists: `mkdir -p storage`

### Connection Refused

- Verify container is running: `docker-compose ps`
- Check health status: `curl http://localhost:5000/api/health`
- Review logs: `docker-compose logs -f rosa-agent`

## Security Considerations

- **API Keys**: Stored locally in container (not in git)
- **Command Whitelist**: Only ROSA/OC/AWS/OCM commands allowed
- **Timeout Protection**: Commands auto-terminate after 60 seconds
- **No Persistence**: Conversation history cleared on restart (stateless)

## Future Enhancements

- [ ] Conversation history persistence
- [ ] Multi-user support with authentication
- [ ] Enhanced knowledge base with RAG
- [ ] Terraform plan generation
- [ ] ROSA cluster status monitoring dashboard
- [ ] Integration with Red Hat SSO

## License

This project is part of the ROSA deployment automation suite.

## Support

For issues or questions:
- Check the [parent project ROSA documentation](../README.md)
- Review [ROSA Cluster creation agent instructions](../ROSA%20Cluster%20creation%20agent%20instructions.md)
- Consult [Red Hat ROSA documentation](https://docs.openshift.com/rosa/)

---

**Built with ❤️ for ROSA operators**
