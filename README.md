# Star Wars Multi-Agent System

This project is a multi-agent system inspired by the Star Wars universe. It features three agents: Anakin Skywalker as the orchestrator, C-3PO for analytical responses, and R2-D2 for technical responses. The system is built with a modular agent framework (ADK) and uses a shared context protocol (MCP) for inter-agent communication. A Streamlit application provides a user interface for interacting with the agents.

## Getting Started

### Prerequisites

- Python 3.7+
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/adk_starwars.git
   cd adk_starwars
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To run the Streamlit application, execute the following command:

```bash
streamlit run app/main.py
```

This will open a new tab in your browser with the application running.

## Framework

This project includes a simple, self-contained agent framework (ADK) and a shared context protocol (MCP). These are not external libraries and do not require separate installation.

- **ADK (Agent Development Kit):** A base `Agent` class (`src/adk/agent.py`) provides a common interface for all agents.
- **MCP (Model Context Protocol):** A simple `MCP` class (`src/adk/mcp.py`) is used for sharing state and context between agents.

## Project Structure

```
.
├── LICENSE
├── README.md
├── app
│   └── main.py         # Streamlit application
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── adk
│   │   ├── __init__.py
│   │   ├── agent.py      # Base agent class
│   │   └── mcp.py        # Shared context protocol
│   └── agents
│       ├── __init__.py
│       ├── anakin.py     # Anakin Skywalker (Orchestrator)
│       ├── c3po.py       # C-3PO (Analytical)
│       └── r2d2.py       # R2-D2 (Technical)
└── tests
    └── test_agents.py    # Unit tests for the agents
```

## The Agents

### Anakin Skywalker (Orchestrator)

Anakin acts as the central orchestrator of the system. He receives user input and, based on keywords, decides which agent is best suited to handle the request.

### C-3PO (Analytical Agent)

C-3PO is specialized in providing formal and analytical responses. He is triggered by keywords such as "risk," "danger," or "formal."

### R2-D2 (Technical Agent)

R2-D2 provides concise and technical responses, often in the form of beeps and boops (with English translations in parentheses). He is triggered by keywords like "technical," "data," or "code."