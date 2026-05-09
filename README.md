# Banking AI Agent

> **Course:** Applications of Natural Language Processing in Industry (CSC15012)  
> **Instructor:** Dr. Nguyễn Hồng Bửu Long  
> **University:** Đại học Khoa học Tự nhiên — ĐHQG TP.HCM

## Overview

An AI Agentic Workflow for banking customer support. The system receives a customer message, runs it through a 6-node pipeline, and returns either a direct reply, a request for more information, or an escalation to a human agent.

## Workflow

```
Customer Message
    → [1] Intent Detection      fine-tuned Llama-3.1-8B (BANKING77, 77 intents)
    → [2] Priority Detection    rules-based: low / medium / high
    → [3] Policy Retrieval      lookup from policies.py (77 banking policies)
    → [4] Response Drafting     gpt-oss:20b via Ollama (streaming)
    → [5] Validation            heuristic quality checks
    → [6] Router                reply / ask_more / escalate
```

```
Customer Message ──→ Intent ──→ Priority ──→ Policy ──→ Draft ──→ Validation ──→ Router
                                                                                    │
                                                        ┌───────────────────────────┤
                                                        ↓           ↓               ↓
                                                    Send Reply  Ask Customer   Escalate
```

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Backend | FastAPI + Python |
| Frontend | Streamlit |
| Intent Detection | Llama-3.1-8B QLoRA (`tunah/banking-intent`) via Colab |
| Response Generation | gpt-oss:20b via Ollama on Colab (streaming) |
| LLM Hosting | Google Colab (T4 GPU) + Pinggy port forwarding |
| Containerization | Docker + Docker Compose |

## Setup

### 1. Clone the repository

```bash
git clone <repo-url>
cd banking-agentic
```

### 2. Configure environment

```bash
cp .env.example .env
```

Edit `.env` with the Pinggy URLs from your two Colab sessions:

```env
OLLAMA_URL=http://your-ollama-pinggy-url.a.free.pinggy.link
OLLAMA_MODEL=gpt-oss:20b
INTENT_API_URL=http://your-intent-pinggy-url.a.free.pinggy.link
```

### 3. Start Colab sessions

**Session 1 — Ollama (gpt-oss:20b):**  
Run `notebooks/Ollama-Pinggy.ipynb` on Colab with T4 GPU. Copy the Pinggy URL → `OLLAMA_URL`.

**Session 2 — Intent Inference Server:**  
Run `notebooks/intent_server.ipynb` on Colab with T4 GPU. Copy the Pinggy URL → `INTENT_API_URL`.

### 4. Run

#### Option A — Docker (recommended)

```bash
docker compose up --build
```

- Backend API: `http://localhost:8000`
- Frontend UI: `http://localhost:8501`

#### Option B — Local

```bash
# Install dependencies
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt

# Start backend
python backend/run.py

# Start frontend (new terminal)
streamlit run frontend/app.py
```

## API Usage

### POST /chat

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "My card was stolen, I need to block it immediately.", "history": []}'
```

**Response:**
```json
{
  "message": "Thank you for contacting us. Your request has been escalated...",
  "action": "escalate",
  "trace": {
    "intent": {"intent": "lost_or_stolen_card", "confidence": 0.97, "top_k": [...]},
    "priority": {"level": "high", "reason": "...", "matched_keywords": ["stolen"]},
    "policy": {"intent": "lost_or_stolen_card", "policy_text": "...", "guidelines": [...]},
    "draft": {"draft_reply": "...", "missing_info": [], "next_action": "block_card"},
    "validation": {"is_valid": true, "issues": [], "should_escalate": true},
    "routing": {"action": "escalate", "final_response": "...", "reason": "..."}
  }
}
```

### POST /chat/stream

Streaming version — returns SSE events:

```
data: {"type": "chunk", "text": "Thank"}
data: {"type": "chunk", "text": " you"}
...
data: {"type": "done", "action": "escalate", "trace": {...}}
```

### GET /health

```bash
curl http://localhost:8000/health
```

## Project Structure

```
banking-agentic/
├── backend/
│   ├── app/
│   │   ├── main.py               # FastAPI app (POST /chat, POST /chat/stream, GET /health)
│   │   ├── core/
│   │   │   ├── settings.py       # Config (reads .env)
│   │   │   └── schemas.py        # Pydantic models
│   │   ├── data/
│   │   │   └── policies.py       # 77 banking policies
│   │   ├── clients/
│   │   │   ├── base.py           # Abstract LLM client
│   │   │   ├── ollama_client.py  # Ollama HTTP client (generate + generate_stream)
│   │   │   └── intent_client.py  # Intent server HTTP client
│   │   ├── nodes/                # 6 pipeline nodes
│   │   └── agent/
│   │       └── orchestrator.py   # Workflow controller (normal + stream)
│   ├── run.py                    # Entry point
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── app.py                    # Streamlit chat UI
│   ├── requirements.txt
│   └── Dockerfile
├── notebooks/
│   ├── intent_server.ipynb       # Colab: intent inference server
│   └── Ollama-Pinggy.ipynb       # Colab: Ollama server
├── examples/
│   └── sample_requests.json      # Test messages
├── docker-compose.yml
├── .env.example
└── .gitignore
```

## Demo Video

*Link will be added after recording.*
