// API base URL
const API_BASE = window.location.origin;

// DOM elements
const messagesContainer = document.getElementById('messages');
const messageInput = document.getElementById('messageInput');
const sendBtn = document.getElementById('sendBtn');
const clearBtn = document.getElementById('clearBtn');
const terminal = document.getElementById('terminal');
const clearTerminalBtn = document.getElementById('clearTerminal');

// Initialize marked.js for markdown rendering
marked.setOptions({
    highlight: function (code, lang) {
        if (lang && hljs.getLanguage(lang)) {
            return hljs.highlight(code, { language: lang }).value;
        }
        return hljs.highlightAuto(code).value;
    },
    breaks: true,
    gfm: true
});

// Auto-resize textarea
messageInput.addEventListener('input', function () {
    this.style.height = 'auto';
    this.style.height = Math.min(this.scrollHeight, 150) + 'px';
});

// Send message on Enter (Shift+Enter for new line)
messageInput.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

// Send button click
sendBtn.addEventListener('click', sendMessage);

// Clear chat button
clearBtn.addEventListener('click', clearChat);

// Clear terminal button
clearTerminalBtn.addEventListener('click', clearTerminal);

// Add to terminal
function addTerminalOutput(command, output, error = null) {
    // Add command
    const cmdLine = document.createElement('div');
    cmdLine.className = 'terminal-line terminal-command';
    cmdLine.textContent = command;
    terminal.appendChild(cmdLine);

    // Add output or error
    if (error) {
        const errorLine = document.createElement('div');
        errorLine.className = 'terminal-line terminal-error';
        errorLine.textContent = error;
        terminal.appendChild(errorLine);
    } else if (output) {
        const outputLine = document.createElement('div');
        outputLine.className = 'terminal-line terminal-output';
        outputLine.textContent = output;
        terminal.appendChild(outputLine);
    }

    // Auto-scroll to bottom
    terminal.scrollTop = terminal.scrollHeight;
}

// Clear terminal
function clearTerminal() {
    terminal.innerHTML = '<div class="terminal-line terminal-info">Terminal cleared.</div>';
}

// Send message function
async function sendMessage() {
    const message = messageInput.value.trim();
    if (!message) return;

    // Disable input while processing
    messageInput.disabled = true;
    sendBtn.disabled = true;

    // Clear input
    messageInput.value = '';
    messageInput.style.height = 'auto';

    // Remove welcome message if present
    const welcome = document.querySelector('.welcome');
    if (welcome) {
        welcome.remove();
    }

    // Add user message to chat
    addMessage('user', message);

    // Show loading indicator
    const loadingId = showLoading();

    try {
        // Send to API
        const response = await fetch(`${API_BASE}/api/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message })
        });

        const data = await response.json();

        // Remove loading indicator
        removeLoading(loadingId);

        if (response.ok && data.success) {
            // If a command was executed, show it in terminal
            if (data.command_executed) {
                const cmdInfo = data.command_executed;

                // Add to terminal
                addTerminalOutput(
                    cmdInfo.command,
                    cmdInfo.success ? cmdInfo.output : null,
                    !cmdInfo.success ? cmdInfo.error : null
                );

                // Also show in chat for context
                let cmdMessage = `**Command Executed:** \`${cmdInfo.command}\`\n\n`;

                if (cmdInfo.success) {
                    cmdMessage += `**Output:**\n\`\`\`\n${cmdInfo.output}\n\`\`\``;
                } else {
                    cmdMessage += `**Error:**\n\`\`\`\n${cmdInfo.error}\n\`\`\``;
                }

                // Add command result as a system-style message
                const cmdDiv = document.createElement('div');
                cmdDiv.className = 'message assistant command-result';

                const cmdAvatar = document.createElement('div');
                cmdAvatar.className = 'message-avatar';
                cmdAvatar.textContent = '⚡';

                const cmdContent = document.createElement('div');
                cmdContent.className = 'message-content';
                cmdContent.innerHTML = marked.parse(cmdMessage);

                cmdDiv.appendChild(cmdAvatar);
                cmdDiv.appendChild(cmdContent);
                messagesContainer.appendChild(cmdDiv);
            }

            // Add assistant response
            addMessage('assistant', data.response);
        } else {
            // Show error
            addMessage('assistant', `❌ Error: ${data.error || 'Failed to get response'}`);
        }
    } catch (error) {
        removeLoading(loadingId);
        addMessage('assistant', `❌ Error: ${error.message}`);
    } finally {
        // Re-enable input
        messageInput.disabled = false;
        sendBtn.disabled = false;
        messageInput.focus();
    }
}

// Add message to chat
function addMessage(role, content) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${role}`;

    const avatar = document.createElement('div');
    avatar.className = 'message-avatar';
    avatar.textContent = role === 'user' ? 'U' : 'AI';

    const messageContent = document.createElement('div');
    messageContent.className = 'message-content';

    // Render markdown for assistant messages
    if (role === 'assistant') {
        messageContent.innerHTML = marked.parse(content);
    } else {
        messageContent.textContent = content;
    }

    messageDiv.appendChild(avatar);
    messageDiv.appendChild(messageContent);

    messagesContainer.appendChild(messageDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

// Show loading indicator
function showLoading() {
    const loadingId = `loading-${Date.now()}`;
    const loadingDiv = document.createElement('div');
    loadingDiv.id = loadingId;
    loadingDiv.className = 'message assistant';

    const avatar = document.createElement('div');
    avatar.className = 'message-avatar';
    avatar.textContent = 'AI';

    const loadingContent = document.createElement('div');
    loadingContent.className = 'message-content';
    loadingContent.innerHTML = `
        <div class="loading">
            <div class="loading-dot"></div>
            <div class="loading-dot"></div>
            <div class="loading-dot"></div>
        </div>
    `;

    loadingDiv.appendChild(avatar);
    loadingDiv.appendChild(loadingContent);

    messagesContainer.appendChild(loadingDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;

    return loadingId;
}

// Remove loading indicator
function removeLoading(loadingId) {
    const loadingDiv = document.getElementById(loadingId);
    if (loadingDiv) {
        loadingDiv.remove();
    }
}

// Clear chat
async function clearChat() {
    if (!confirm('Are you sure you want to clear the chat history?')) {
        return;
    }

    try {
        await fetch(`${API_BASE}/api/conversation/clear`, {
            method: 'POST'
        });

        // Clear messages
        messagesContainer.innerHTML = `
            <div class="welcome">
                <h2>Welcome to ROSA AI Agent</h2>
                <p>Your expert assistant for Red Hat OpenShift Service on AWS</p>
                <p style="margin-top: 1rem; font-size: 0.9rem;">Ask me anything about ROSA cluster deployment, CLI commands, or troubleshooting!</p>
            </div>
        `;

        // Also clear terminal
        clearTerminal();
    } catch (error) {
        console.error('Failed to clear chat:', error);
    }
}

// Check health on load
async function checkHealth() {
    try {
        const response = await fetch(`${API_BASE}/api/health`);
        const data = await response.json();

        if (!response.ok || data.status !== 'healthy') {
            console.warn('Backend health check failed:', data);
        } else {
            console.log('Backend is healthy:', data);
        }
    } catch (error) {
        console.error('Health check failed:', error);
    }
}

// Initialize
checkHealth();
messageInput.focus();
