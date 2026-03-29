# ARIA: AI Reliable Agent Infrastructure

## Overview

ARIA (AI Reliable Agent Infrastructure) is an innovative AI agent orchestration system designed for resilient invoice processing workflows. Built as an MVP for the GenAI Hackathon, ARIA demonstrates advanced concepts in AI reliability, self-healing systems, and real-time monitoring. The system uses modular agents, retry policies, confidence scoring, and audit logging to ensure robust execution even in the face of failures.

### Key Features
- **Modular Agent Architecture**: Extensible base agents for different tasks (e.g., invoice processing, verification).
- **Self-Healing Orchestration**: Automatic failure detection, classification, and recovery (retries, data fixes).
- **Confidence Scoring**: Evaluates output quality to flag low-confidence results for escalation.
- **Real-Time Audit Logging**: SQLite-based logging with a live web dashboard for monitoring.
- **Web Dashboard**: Interactive frontend for visualizing agent activities and system health.
- **REST API**: FastAPI-based endpoints for log retrieval and potential future integrations.

### Hackathon Context
This MVP showcases GenAI principles by simulating intelligent, adaptive AI agents in a business workflow. It addresses real-world challenges like error handling in AI systems, making it suitable for enterprise applications such as automated document processing, financial workflows, or any scenario requiring reliable AI orchestration.

## Project Structure

```
ARIA/
├── main.py                 # Entry point for console demo
├── requirements.txt        # Python dependencies
├── audit/
│   └── logger.py          # Audit logging to SQLite database
├── core/
│   ├── base_agent.py      # Base agent class with confidence calculation
│   ├── confidence.py      # Confidence scoring logic
│   ├── orchestrator/
│   │   └── main.py        # Main orchestration logic (execute, retry, verify)
│   └── retry_policy.py    # Failure classification and recovery strategies
├── agents/
│   └── process_orchestration/
│       ├── invoice_agent.py    # Invoice processing agent
│       └── verifier_agent.py   # Result verification agent
├── api/
│   ├── server.py          # FastAPI server with CORS
│   └── index.html         # Basic web dashboard (legacy)
└── frontend/              # Enhanced web dashboard
    ├── index.html
    ├── style.css
    └── script.js
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps
1. Clone or navigate to the project directory:
   ```
   cd P:\ET GenAI\ARIA
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. (Optional) If using a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   pip install -r requirements.txt
   ```

## Usage

### Running the Console Demo
The demo showcases the full orchestration workflow with intentional failures to demonstrate self-healing.

1. Run the demo:
   ```
   python main.py
   ```

2. Expected Output:
   - System initialization
   - Invoice data processing
   - Failure handling and recovery
   - Verification and final results
   - Audit logs printed to console

### Running the Web Dashboard
For real-time monitoring of agent activities:

1. Start the FastAPI server:
   ```
   uvicorn api.server:app --reload
   ```
   - Server runs on `http://127.0.0.1:8000`

2. Open the enhanced dashboard:
   - Navigate to `frontend/index.html` and open in a browser
   - Or visit `http://127.0.0.1:8000` (serves basic dashboard)

3. Generate activity:
   - In another terminal, run `python main.py` to populate logs

### API Endpoints

- `GET /logs`: Retrieve recent audit logs (JSON format)
  - Response: `{"logs": [{"id": 1, "timestamp": "...", "agent": "...", "event": "...", "payload": "..."}]}`
  - Used by the web dashboard for real-time updates

## Architecture Details

### Core Components
- **Orchestrator**: Central controller that executes agents, handles exceptions, and coordinates retries/verification.
- **Agents**: Implement `BaseAgent` with a `think()` method. Outputs include confidence scores.
- **Retry Engine**: Classifies failures (transient, data error) and applies fixes (e.g., auto-generating missing PO numbers).
- **Audit Logger**: Logs all events to SQLite (`audit.db`) for traceability.
- **Confidence Calculator**: Simple heuristic-based scoring (length, error absence).

### Workflow Example
1. Orchestrator receives invoice data
2. Executes InvoiceAgent → Fails due to missing PO
3. RetryEngine classifies as "DATA_ERROR" → Fixes data
4. Re-executes → Succeeds
5. VerifierAgent validates output
6. Logs everything; escalates if confidence < 60%

### Technologies Used
- **Backend**: Python, FastAPI, Uvicorn, SQLite
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Libraries**: sqlite3 (built-in), fastapi, uvicorn, flask-cors

## Development

### Extending the System
- Add new agents by inheriting `BaseAgent` and implementing `think()`.
- Enhance retry policies in `retry_policy.py`.
- Modify confidence logic in `confidence.py`.
- Add API endpoints in `api/server.py`.

### Testing
- Run the demo: `python main.py`
- Check logs in `audit.db` or via API
- Test dashboard by running server and opening frontend

### Known Limitations (MVP Scope)
- Simple confidence scoring (can be upgraded to ML-based)
- Basic verification (expand to more complex rules)
- No authentication or security features
- SQLite for demo; scale to PostgreSQL for production

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make changes and test
4. Submit a pull request

## Hackathon Submission Notes
- **Innovation**: Demonstrates AI resilience and orchestration for business workflows.
- **Scalability**: Modular design allows easy extension to other domains.
- **Real-World Impact**: Addresses AI reliability issues in enterprise automation.
- **Future Enhancements**: Integrate with LLMs for smarter agents, add user authentication, deploy to cloud.

For questions or feedback, contact the development team.