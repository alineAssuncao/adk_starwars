
# Sistema Multiagente Star Wars

Este projeto é um sistema multiagente inspirado no universo Star Wars. Ele apresenta três agentes: Anakin Skywalker como orquestrador, C-3PO para respostas analíticas e R2-D2 para respostas técnicas. O sistema é construído com um framework modular de agentes (ADK) e utiliza um protocolo de contexto compartilhado (MCP) para comunicação entre agentes. Uma aplicação Streamlit fornece uma interface de usuário para interagir com os agentes.

## Primeiros Passos

### Pré-requisitos

- Python 3.7+
- pip

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/your-username/adk_starwars.git
   cd adk_starwars
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

### Executando a Aplicação

Para rodar a aplicação Streamlit, execute o seguinte comando:

```bash
streamlit run app/main.py
```

Isso abrirá uma nova aba no seu navegador com a aplicação em execução.

## Framework

Este projeto inclui um framework de agentes simples e auto-contido (ADK) e um protocolo de contexto compartilhado (MCP). Estes não são bibliotecas externas e não requerem instalação separada.

- **ADK (Agent Development Kit):** Uma classe base `Agent` (`src/adk/agent.py`) fornece uma interface comum para todos os agentes.
- **MCP (Model Context Protocol):** Uma classe simples `MCP` (`src/adk/mcp.py`) é usada para compartilhar estado e contexto entre os agentes.

## Estrutura do Projeto

```
.
├── LICENSE
├── README.md
├── app
│   └── main.py         # Aplicação Streamlit
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── adk
│   │   ├── __init__.py
│   │   ├── agent.py      # Classe base de agente
│   │   └── mcp.py        # Protocolo de contexto compartilhado
│   └── agents
│       ├── __init__.py
│       ├── anakin.py     # Anakin Skywalker (Orquestrador)
│       ├── c3po.py       # C-3PO (Analítico)
│       └── r2d2.py       # R2-D2 (Técnico)
└── tests
    └── test_agents.py    # Testes unitários dos agentes
```

## Os Agentes

### Anakin Skywalker (Orquestrador)

Anakin atua como o orquestrador central do sistema. Ele recebe a entrada do usuário e, com base em palavras-chave, decide qual agente é mais adequado para lidar com a solicitação.

### C-3PO (Agente Analítico)

C-3PO é especializado em fornecer respostas formais e analíticas. Ele é acionado por palavras-chave como "risco", "perigo" ou "formal".

### R2-D2 (Agente Técnico)

R2-D2 fornece respostas concisas e técnicas, muitas vezes na forma de bipes e sons (com traduções em português entre parênteses). Ele é acionado por palavras-chave como "técnico", "dados" ou "código".
