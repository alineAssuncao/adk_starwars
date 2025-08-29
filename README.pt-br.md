# 🪐 Sistema Multiagente Star Wars — IA Autônoma com ADK, MCP e Jules[bot]

## 💡 Descrição

Este projeto é um sistema multiagente inspirado no universo Star Wars, desenvolvido com foco em simulação de inteligência distribuída. Ele apresenta três agentes principais:

- **Anakin Skywalker** — Orquestrador central
- **C-3PO** — Agente analítico
- **R2-D2** — Agente técnico

Cada agente possui um papel distinto e responde a comandos com base em palavras-chave específicas. A comunicação entre eles é feita por meio de um protocolo de contexto compartilhado (MCP), e a interação com o usuário é realizada através de uma interface web construída com **Streamlit**.

Além disso, o projeto integra o **google-labs-jules[bot]**, um agente generativo que atua como coordenador inteligente, interpretando comandos em linguagem natural e delegando ações aos agentes temáticos.

---

## 🤖 Arquitetura de Agentes

### ADK (Agent Development Kit)
Um framework modular e auto-contido que define a estrutura base dos agentes.  
- Local: `src/adk/agent.py`  
- Função: Interface comum para todos os agentes

### MCP (Model Context Protocol)
Protocolo simples para compartilhamento de estado e contexto entre os agentes.  
- Local: `src/adk/mcp.py`  
- Função: Comunicação entre agentes e orquestração de decisões

---

## 🧠 Os Agentes

| Agente         | Função | Palavras-chave |
|----------------|--------|----------------|
| **Anakin**     | Orquestrador | Decide qual agente deve responder |
| **C-3PO**      | Analítico | "risco", "perigo", "formal" |
| **R2-D2**      | Técnico | "técnico", "dados", "código" |

R2-D2 responde com sons técnicos (bipes), traduzidos em português entre parênteses para facilitar a compreensão.

---

## 🖥️ Interface com Streamlit

A aplicação inclui uma interface web interativa para comunicação com os agentes.  
Ao executar, uma aba será aberta no navegador com a simulação em tempo real.

---

## 🚀 Primeiros Passos

### ✅ Pré-requisitos
- Python 3.7+
- pip

### 📦 Instalação

```bash
git clone https://github.com/alineAssuncao/adk_starwars.git
cd adk_starwars
pip install -r requirements.txt
```

### ▶️ Executando a Aplicação
```Bash
streamlit run app/main.py
```

## 🗂️ Estrutura do Projeto
```
.
├── LICENSE
├── README.md
├── app
│   └── main.py               # Aplicação Streamlit
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── adk
│   │   ├── __init__.py
│   │   ├── agent.py          # Classe base de agente
│   │   └── mcp.py            # Protocolo de contexto compartilhado
│   └── agents
│       ├── __init__.py
│       ├── anakin.py         # Anakin Skywalker (Orquestrador)
│       ├── c3po.py           # C-3PO (A
```


## 📚 Aprendizados
- Modelagem de agentes com ADK
- Comunicação entre agentes via MCP
- Integração de LLMs com agentes temáticos
- Interface interativa com Streamlit
- Design de sistemas multiagente com propósito narrativo

## 🔮 Próximos Passos
- Adicionar novos agentes com funções especializadas
- Criar missões colaborativas entre agentes
- Integrar LangChain ou CrewAI para fluxos mais complexos
- Implementar visualizações de comportamento em tempo real


## 👩‍💻 Autora

Aline Assunção

Engenheira de Qualidade em transição para Inteligência Artificial

📫 [LinkedIn](https://www.linkedin.com/in/alineassuncaoai/)  

📬 aline.jassuncao@gmail.com

>_"A imaginação é o combustível da inovação. E aqui, ela vem com sabres de luz e agentes inteligentes."_













