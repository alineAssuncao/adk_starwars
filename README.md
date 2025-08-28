# 🪐 Star Wars Multi-Agent System — Autonomous AI with ADK, MCP and Jules[bot]

## 💡 Overview

This project is a multi-agent system inspired by the Star Wars universe, designed to simulate distributed intelligence. It features three main agents:

- **Anakin** — Central orchestrator  
- **C-3PO** — Analytical agent  
- **R2-D2** — Technical agent  

Each agent plays a distinct role and responds to user input based on specific keywords. Communication between agents is handled through a shared context protocol (MCP), and user interaction is provided via a web interface built with **Streamlit**.

The project also integrates **google-labs-jules[bot]**, a generative agent that interprets natural language commands and delegates tasks to the themed agents, enhancing the system's intelligence and flexibility.

---

## 🤖 Agent Architecture

### ADK (Agent Development Kit)  
A modular, self-contained framework that defines the base structure for agents.  
- Location: `src/adk/agent.py`  
- Purpose: Provides a common interface for all agents

### MCP (Model Context Protocol)  
A lightweight protocol for sharing state and context between agents.  
- Location: `src/adk/mcp.py`  
- Purpose: Enables communication and decision orchestration

---

## 🧠 The Agents

| Agent         | Role         | Trigger Keywords         |
|---------------|--------------|--------------------------|
| **Anakin**    | Orchestrator | Routes requests to agents |
| **C-3PO**     | Analytical   | "risk", "danger", "formal" |
| **R2-D2**     | Technical    | "technical", "data", "code" |

R2-D2 responds with technical beeps and sounds (translated into Portuguese for clarity).

---

## 🖥️ Streamlit Interface

The project includes an interactive web interface built with Streamlit, allowing users to communicate with the agents in real time.  
Running the app will open a browser tab with the simulation.

---

## 🚀 Getting Started

### ✅ Prerequisites
- Python 3.7+
- pip

### 📦 Installation

```bash
git clone https://github.com/alineAssuncao/adk_starwars.git
cd adk_starwars
pip install -r requirements.txt
```

### ▶️ Running the Application

```
streamlit run app/main.py
```

## 🗂️ Project Structure
```
.
├── LICENSE
├── README.md
├── app
│   └── main.py               # Streamlit application
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── adk
│   │   ├── __init__.py
│   │   ├── agent.py          # Base agent class
│   │   └── mcp.py            # Shared context protocol
│   └── agents
│       ├── __init__.py
│       ├── anakin.py         # Anakin Skywalker (Orchestrator)
│       ├── c3po.py           # C-3PO (Analytical)
│       └── r2d2.py           # R2-D2 (Technical)
└── tests
    └── test_agents.py        # Unit tests for agents
```

## 📚 Key Learnings
- Agent modeling with ADK
- Inter-agent communication via MCP
- Integration of LLMs with themed agents
- Interactive UI with Streamlit
- Designing narrative-driven multi-agent systems

## 🔮 Next Steps
- Add new agents with specialized roles
- Create collaborative missions between agents
- Integrate LangChain or CrewAI for more complex workflows
- Implement real-time behavior visualizations


## 👩‍💻 Author
Aline Assunção
Quality Engineer transitioning into Artificial Intelligence

📫 [LinkedIn](https://www.linkedin.com/in/alineassuncaoai/)  
📬 aline.jassuncao@gmail.com

---

> _"Imagination fuels innovation. And here, it comes with lightsabers and intelligent agents."_ 
