// API base URL
const API_BASE = window.location.origin;

// DOM elements
const providerSelect = document.getElementById('provider');
const settingsForm = document.getElementById('settingsForm');
const testBtn = document.getElementById('testBtn');
const alertContainer = document.getElementById('alertContainer');
const systemInfo = document.getElementById('systemInfo');

// Provider config containers
const groqConfig = document.getElementById('groqConfig');
const openaiConfig = document.getElementById('openaiConfig');
const anthropicConfig = document.getElementById('anthropicConfig');
const localConfig = document.getElementById('localConfig');

// Show/hide provider configs
providerSelect.addEventListener('change', function () {
    const provider = this.value;

    // Hide all configs
    groqConfig.style.display = 'none';
    openaiConfig.style.display = 'none';
    anthropicConfig.style.display = 'none';
    localConfig.style.display = 'none';

    // Show selected config
    if (provider === 'groq') {
        groqConfig.style.display = 'block';
    } else if (provider === 'openai') {
        openaiConfig.style.display = 'block';
    } else if (provider === 'anthropic') {
        anthropicConfig.style.display = 'block';
    } else if (provider === 'local') {
        localConfig.style.display = 'block';
    }
});

// Load current settings
async function loadSettings() {
    try {
        const response = await fetch(`${API_BASE}/api/settings`);
        const data = await response.json();

        if (response.ok) {
            // Set provider
            providerSelect.value = data.provider;
            providerSelect.dispatchEvent(new Event('change'));

            // Set provider-specific config
            const config = data.config || {};

            if (data.provider === 'groq') {
                document.getElementById('groqApiKey').value = config.api_key || '';
                document.getElementById('groqModel').value = config.model || 'llama-3.1-8b-instant';
            } else if (data.provider === 'openai') {
                document.getElementById('openaiApiKey').value = config.api_key || '';
                document.getElementById('openaiModel').value = config.model || 'gpt-4';
            } else if (data.provider === 'anthropic') {
                document.getElementById('anthropicApiKey').value = config.api_key || '';
                document.getElementById('anthropicModel').value = config.model || 'claude-3-sonnet-20240229';
            } else if (data.provider === 'local') {
                document.getElementById('localEndpoint').value = config.endpoint_url || '';
                document.getElementById('localApiKey').value = config.api_key || '';
                document.getElementById('localModel').value = config.model || 'llama2';
            }
        }
    } catch (error) {
        showAlert('error', `Failed to load settings: ${error.message}`);
    }
}

// Save settings
settingsForm.addEventListener('submit', async function (e) {
    e.preventDefault();

    const provider = providerSelect.value;
    let config = {};

    // Get provider-specific config
    if (provider === 'groq') {
        config = {
            api_key: document.getElementById('groqApiKey').value,
            model: document.getElementById('groqModel').value
        };
    } else if (provider === 'openai') {
        config = {
            api_key: document.getElementById('openaiApiKey').value,
            model: document.getElementById('openaiModel').value
        };
    } else if (provider === 'anthropic') {
        config = {
            api_key: document.getElementById('anthropicApiKey').value,
            model: document.getElementById('anthropicModel').value
        };
    } else if (provider === 'local') {
        config = {
            endpoint_url: document.getElementById('localEndpoint').value,
            api_key: document.getElementById('localApiKey').value,
            model: document.getElementById('localModel').value
        };
    }

    // Validate required fields
    if (provider === 'groq' && !config.api_key) {
        showAlert('error', 'Groq API key is required');
        return;
    }
    if (provider === 'openai' && !config.api_key) {
        showAlert('error', 'OpenAI API key is required');
        return;
    }
    if (provider === 'anthropic' && !config.api_key) {
        showAlert('error', 'Anthropic API key is required');
        return;
    }
    if (provider === 'local' && !config.endpoint_url) {
        showAlert('error', 'Endpoint URL is required for local models');
        return;
    }

    try {
        const response = await fetch(`${API_BASE}/api/settings`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ provider, config })
        });

        const data = await response.json();

        if (response.ok && data.success) {
            showAlert('success', 'Settings saved successfully! You can now use the chat.');
            // Reload settings to show masked API key
            setTimeout(loadSettings, 1000);
        } else {
            showAlert('error', data.error || 'Failed to save settings');
        }
    } catch (error) {
        showAlert('error', `Failed to save settings: ${error.message}`);
    }
});

// Test connection
testBtn.addEventListener('click', async function () {
    const provider = providerSelect.value;
    let config = {};

    // Get provider-specific config
    if (provider === 'groq') {
        config = {
            api_key: document.getElementById('groqApiKey').value,
            model: document.getElementById('groqModel').value
        };
    } else if (provider === 'openai') {
        config = {
            api_key: document.getElementById('openaiApiKey').value,
            model: document.getElementById('openaiModel').value
        };
    } else if (provider === 'anthropic') {
        config = {
            api_key: document.getElementById('anthropicApiKey').value,
            model: document.getElementById('anthropicModel').value
        };
    } else if (provider === 'local') {
        config = {
            endpoint_url: document.getElementById('localEndpoint').value,
            api_key: document.getElementById('localApiKey').value,
            model: document.getElementById('localModel').value
        };
    }

    testBtn.disabled = true;
    testBtn.textContent = 'Testing...';

    try {
        const response = await fetch(`${API_BASE}/api/settings`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                provider,
                config,
                test_connection: true
            })
        });

        const data = await response.json();

        if (response.ok && data.success) {
            showAlert('success', 'Connection test successful!');
        } else {
            showAlert('error', data.error || 'Connection test failed');
        }
    } catch (error) {
        showAlert('error', `Connection test failed: ${error.message}`);
    } finally {
        testBtn.disabled = false;
        testBtn.textContent = 'Test Connection';
    }
});

// Show alert
function showAlert(type, message) {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type}`;
    alertDiv.textContent = message;

    alertContainer.innerHTML = '';
    alertContainer.appendChild(alertDiv);

    // Auto-hide after 5 seconds
    setTimeout(() => {
        alertDiv.remove();
    }, 5000);
}

// Load system information
async function loadSystemInfo() {
    try {
        const response = await fetch(`${API_BASE}/api/health`);
        const data = await response.json();

        if (response.ok) {
            systemInfo.innerHTML = `
                <div style="display: grid; gap: 1rem;">
                    <div>
                        <strong style="color: var(--text-primary);">Status:</strong>
                        <span style="color: var(--success-green);">${data.status}</span>
                    </div>
                    <div>
                        <strong style="color: var(--text-primary);">Current Provider:</strong>
                        <span style="color: var(--text-secondary);">${data.provider}</span>
                    </div>
                    <div>
                        <strong style="color: var(--text-primary);">CLI Tools:</strong>
                        <ul style="margin-top: 0.5rem; padding-left: 1.5rem; color: var(--text-secondary);">
                            ${Object.entries(data.cli_tools || {}).map(([tool, version]) =>
                `<li><code style="color: var(--primary-red);">${tool}</code>: ${version.split('\n')[0]}</li>`
            ).join('')}
                        </ul>
                    </div>
                </div>
            `;
        }
    } catch (error) {
        systemInfo.innerHTML = `<p style="color: var(--error-red);">Failed to load system information</p>`;
    }
}

// Initialize
loadSettings();
loadSystemInfo();
