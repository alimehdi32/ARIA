# 🚀 ZYAI – Reliable Agentic AI Framework

ZYAI is a resilient AI orchestration framework designed to improve the reliability, observability, and fault tolerance of AI-powered workflows.

Unlike traditional AI applications that fail when encountering incomplete or invalid inputs, ZYAI introduces self-healing execution pipelines, confidence estimation, verification layers, and workflow monitoring to ensure reliable AI system behavior.

---

# ✨ Features

## 🤖 Agent-Based Architecture

Modular AI agents designed for specialized workflow execution.

* Invoice Processing Agent
* Verification Agent
* Confidence Evaluation Engine
* Retry & Recovery Engine

---

## 🔄 Self-Healing Workflows

ZYAI automatically detects workflow failures and applies recovery strategies.

Example:

```text
Missing PO Number
        ↓
Failure Detection
        ↓
Automatic Data Repair
        ↓
Workflow Re-Execution
        ↓
Successful Completion
```

---

## 🛡 Failure Classification

The framework classifies failures into categories:

* DATA_ERROR
* TRANSIENT_ERROR
* UNKNOWN_ERROR

Each category follows a dedicated recovery strategy.

---

## 📊 Confidence Scoring

ZYAI evaluates output quality using a confidence estimation engine.

Applications:

* Human-in-the-loop systems
* Escalation workflows
* Reliability assessment
* Output validation

---

## ✅ Verification Layer

Outputs pass through a verification stage before final delivery.

Benefits:

* Improved reliability
* Reduced invalid responses
* Better workflow trustworthiness

---

## 📜 Audit Logging

Every workflow event is recorded.

Examples:

* START
* FAILURE
* RECOVERY_SUCCESS
* SUCCESS
* VERIFICATION

---

## 📈 Monitoring Dashboard

Real-time dashboard built with:

* HTML
* CSS
* JavaScript
* FastAPI

Provides:

* Workflow visibility
* Event monitoring
* System observability
* Audit history

---

# 🏗 System Architecture

```text
                 User Input
                      │
                      ▼
               Invoice Agent
                      │
              Failure?
             /       \
           Yes        No
           │           │
           ▼           ▼
      Retry Engine   Success
           │
      Auto Recovery
           │
           ▼
      Verification
           │
           ▼
   Confidence Scoring
           │
           ▼
      Audit Logging
           │
           ▼
        Dashboard
```

---

# 📂 Project Structure

```text
ZYAI/
│
├── main.py
├── requirements.txt
│
├── agents/
│   └── process_orchestration/
│       ├── invoice_agent.py
│       └── verifier_agent.py
│
├── audit/
│   └── logger.py
│
├── core/
│   ├── base_agent.py
│   ├── confidence.py
│   ├── retry_policy.py
│   │
│   └── orchestrator/
│       └── main.py
│
├── api/
│   ├── __init__.py
│   └── server.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── audit.db
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/your-username/ZYAI.git
cd ZYAI
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Running ZYAI

## Console Demo

```bash
python main.py
```

Example Input:

```text
Vendor Name: Amazon
Amount: 15000
PO Number:
```

Example Output:

```text
Failure Detected
Auto-Recovery Triggered
Invoice Successfully Processed
Confidence Score: 0.88
```

---

## Start API Server

```bash
uvicorn api.server:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

## Launch Dashboard

Open:

```text
frontend/index.html
```

The dashboard displays:

* System Events
* Success Rate
* Failures
* Confidence Metrics
* Workflow Logs

---

# 📌 Example Workflow

Input:

```json
{
  "vendor": "Amazon",
  "amount": 15000,
  "po_number": null
}
```

Execution:

```text
Invoice Agent
      ↓
Failure Detected
      ↓
Retry Engine
      ↓
PO Auto Generated
      ↓
Verification
      ↓
Confidence Scoring
      ↓
Success
```

Output:

```json
{
  "status": "SUCCESS",
  "confidence": 0.88
}
```

---

# 🧠 Technology Stack

## Backend

* Python
* FastAPI
* SQLite

## AI & ML

* Scikit-Learn
* Confidence Scoring Engine
* Agent-Based Workflow Execution

## Frontend

* HTML
* CSS
* JavaScript

## Infrastructure

* REST APIs
* Audit Logging
* Workflow Monitoring

---

# 📋 Current Capabilities

✅ Agent Orchestration

✅ Workflow Monitoring

✅ Self-Healing Retries

✅ Confidence Scoring

✅ Failure Classification

✅ Verification Pipeline

✅ FastAPI Dashboard

✅ Audit Logging

---

# 🔮 Roadmap

## Agentic RAG

* ChromaDB Integration
* Embedding-Based Retrieval
* Semantic Search
* Context Grounding

## Multi-Agent Systems

* Retrieval Agent
* Planning Agent
* Reasoning Agent
* Evaluation Agent

## Enterprise Features

* Authentication
* PostgreSQL Support
* Cloud Deployment
* Workflow Analytics
* RBAC

---

# 🎯 Vision

Most AI projects focus on generating outputs.

ZYAI focuses on ensuring those outputs are:

* Reliable
* Recoverable
* Verifiable
* Observable

The long-term vision is to evolve ZYAI into a complete Agentic AI platform capable of orchestrating retrieval, reasoning, verification, and self-healing workflows at scale.

---

# 👨‍💻 Author

**Afraaz Ul Haque**

GitHub: https://github.com/AfraazUlHaque

LinkedIn: https://www.linkedin.com/in/afraazul-haque-5b668a325
