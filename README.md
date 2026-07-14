# 🧠 AI Memory Agent

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com/)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-orange.svg)](https://ollama.com)

> **Persistent memory for AI coding assistants.** 

AI Memory Agent stores project knowledge outside the LLM's temporary context window and automatically rebuilds context for fresh conversations. Stop explaining your codebase architecture, completed work, or project rules every time you open a new chat.

---

## ✨ Why AI Memory Agent?

Instead of starting every single conversation from scratch, the agent continuously tracks and injects:

*   **Project Summary:** High-level overview and core business logic.
*   **Completed Work:** What has already been built so the AI doesn't duplicate code.
*   **Active Sprint/Task:** The immediate objective you are working on.
*   **Architecture & Tech Decisions:** Design patterns, chosen libraries, and constraints.
*   **Repository Analysis:** Key modules, file structures, and entry points.

The result is a local, secure AI assistant that carries context seamlessly across unlimited chats.

---

## 🛠️ Tech Stack

| Layer | Technology | Details |
|---|---|---|
| **Backend** | Python 3.10+, FastAPI, Pydantic | Includes an AST Parser for code structure extraction. |
| **LLM Engine** | Ollama | Runs 100% locally with `qwen3:8b` or other open weights. |
| **Frontend** | Chrome Extension | Injects parsed memory directly into Claude's UI. |
| **Storage** | Local JSON | Simple, git-trackable, zero complex cloud dependencies. |

---

## 📐 System Architecture

Below is the conceptual flow of how the agent intercepts, analyzes, and reinjects context.

```text
   ┌────────────────────────┐
   │    Claude Chat (Web)   │
   └───────────┬────────────┘
               │  (1) Capture conversation
               ▼
   ┌────────────────────────┐
   │    Chrome Extension    │
   └───────────┬────────────┘
               │  (2) HTTP POST /memory/event
               ▼
   ┌────────────────────────┐
   │    FastAPI Backend     │
   └─────┬───────────┬──────┘
         │           │
┌─────────┘           └─────────┐
│ (Internal Scan)               │ (Analyze via Local LLM)
▼                               ▼
┌──────────────────────┐   ┌──────────────────────┐
│  Repository Scanner  │   │      Local Ollama    │
│  (Code AST Parser)   │   │      (qwen3:8b)      │
└─────────┬────────────┘   └───────────┬──────────┘
│                            │
▼                            ▼
┌──────────────────────┐   ┌──────────────────────┐
│ Repository Analysis  │   │    Change Extractor  │
└─────────┬────────────┘   └───────────┬──────────┘
│                            │
└────────────┬───────────────┘
│ (Memory Merger)
▼
┌───────────────────────────┐
│    project_memory.json    │
└─────────────┬─────────────┘
│
▼
┌───────────────────────────┐
│      Context Generator    │
└─────────────┬─────────────┘
│  (3) Auto-injects payload
▼
┌────────────────────────┐
│  New Claude Chat Window│
└────────────────────────┘
```

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/othmanekabbaj/ai-memory-agent.git
cd ai-memory-agent
```

### 2. Set Up Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS (Bash):**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Backend Dependencies
```bash
pip install -r backend/requirements.txt
```

### 4. Configure & Run Ollama
Download and install [Ollama](https://ollama.com/). Pull your local LLM model of choice:
```bash
ollama pull qwen3:8b
```

### 5. Launch the Backend API
```bash
cd backend
uvicorn main:app --reload
```
*The server will boot up at `http://localhost:8000`.*

### 6. Install the Chrome Extension
1. Open Google Chrome and navigate to `chrome://extensions/`.
2. Toggle **Developer mode** (top-right corner) to ON.
3. Click **Load unpacked** (top-left corner).
4. Select the directory: `extensions/claude-memory`.

---

## 🔌 API & Script Usage

### Triggering a Repository Scan
To manually analyze and index a local codebase directory:

```python
from backend.services.repository import RepositoryService

RepositoryService().scan_repository("path/to/your/project")
```

### Key API Endpoints
*   `POST /memory/event` — Emitted by the Chrome extension to process a fresh message block.
*   `GET /memory/context` — Computes and generates the Markdown context payload ready for injection.

---

## 🗺️ Product Roadmap

- [x] **Local Core:** Persistent local memory engine
- [x] **Privacy-First LLM:** Seamless local integration with Ollama
- [x] **AST Parser:** Static analysis codebase repository scanning
- [ ] **Git Hooks:** Auto-update memory on git commit or checkout changes
- [ ] **VSCode Extension:** Native sidebar to inspect active memories
- [ ] **Semantic Memory:** Vector storage support (Chroma/Qdrant)
- [ ] **Multi-Project Management:** Easily swap profiles per repository
- [ ] **Extended Clients:** Native Desktop integration (Cursor, Windsurf, Claude Desktop)
