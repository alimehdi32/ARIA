// ARIA Dashboard Script

const API_URL = 'http://127.0.0.1:8000/logs';
let stats = { total: 0, success: 0, failure: 0 };

async function fetchLogs() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        updateLogs(data.logs);
        updateStats(data.logs);
    } catch (error) {
        console.error('Failed to fetch logs:', error);
        document.getElementById('logs-container').innerHTML = '<div class="log FAILURE"><strong>Error:</strong> Unable to fetch logs. Ensure the server is running.</div>';
    }
}

function updateLogs(logs) {
    const container = document.getElementById('logs-container');
    container.innerHTML = '';

    if (logs.length === 0) {
        container.innerHTML = '<div class="log">No logs available yet. Run the demo to generate logs.</div>';
        return;
    }

    logs.forEach(log => {
        const logDiv = document.createElement('div');
        logDiv.className = `log ${log.event}`;

        logDiv.innerHTML = `
            <strong>${log.agent}</strong> - ${log.event}<br/>
            <small>${new Date(log.timestamp).toLocaleString()}</small><br/>
            <code>${log.payload}</code>
        `;

        container.appendChild(logDiv);
    });
}

function updateStats(logs) {
    stats.total = logs.length;
    stats.success = logs.filter(log => log.event === 'SUCCESS').length;
    stats.failure = logs.filter(log => log.event === 'FAILURE').length;

    document.getElementById('total-logs').textContent = stats.total;
    document.getElementById('success-count').textContent = stats.success;
    document.getElementById('failure-count').textContent = stats.failure;
}

// Fetch logs on page load and every 2 seconds
fetchLogs();
setInterval(fetchLogs, 2000);