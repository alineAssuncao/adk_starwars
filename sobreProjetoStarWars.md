# Sobre o Projeto Star Wars Multi-Agent System

## Visão Geral

Este projeto é um sistema de agentes inteligentes inspirado no universo Star Wars, que utiliza tecnologias de ponta em inteligência artificial e arquitetura de software. Ele integra múltiplos agentes (Anakin, C3PO, R2D2) que interagem entre si e com o usuário, empregando modelos generativos de linguagem (LLM) para respostas dinâmicas e contextuais.

O sistema é construído sobre o ADK (Agent Development Kit), um framework modular para criação e orquestração de agentes inteligentes, e o MCP (Model Context Protocol), que provê memória compartilhada e contexto global para todos os agentes. Essa combinação permite conversas naturais, colaboração entre agentes e fácil extensibilidade para novas funcionalidades.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do backend e dos agentes.
- **Streamlit**: Framework para criar interfaces web interativas de forma rápida e simples.
- **google-generativeai**: Biblioteca para acessar modelos LLM (como Gemini) da Google, usada para gerar respostas inteligentes dos agentes.
- **dotenv**: Para carregar variáveis de ambiente (como chaves de API) de um arquivo `.env` de forma segura.

## Estrutura do Projeto

- `app/main.py`: Interface e orquestração do chat multiagente.
- `src/agents/`: Implementação dos agentes (Anakin, C3PO, R2D2).
- `src/adk/mcp.py`: Contexto compartilhado entre agentes (Model Context Protocol).
- `requirements.txt`: Dependências do projeto.
- `.env`: Armazena chaves e variáveis sensíveis (não versionado).

## Lógica e Arquitetura

### Interface Multiagente
- O usuário escolhe com qual agente quer conversar usando um seletor (`st.radio`).
- Cada agente tem seu próprio histórico de mensagens, exibido de forma alinhada e estilizada.
- A interface troca automaticamente para o agente que respondeu, tornando a experiência fluida.

### Envio e Roteamento de Mensagens
- Ao enviar uma mensagem, ela é registrada no histórico do agente selecionado.
- O agente correspondente é chamado para gerar a resposta:
  - Se for o Anakin, usa o objeto `AnakinAgent`.
  - Se for C3PO ou R2D2, a mensagem é roteada via Anakin, que decide quem responde.
- A resposta pode vir com um prefixo indicando o agente (ex: `C3PO: resposta...`).

### Detecção e Troca de Agente
- O código detecta, pelo prefixo da resposta, qual agente está respondendo.
- Se o prefixo for reconhecido (ex: `C3PO`, `C3-PO`, `R2D2`, etc.), a resposta é registrada no histórico do agente correto e a interface troca automaticamente para esse agente.
- Se não houver prefixo, a resposta fica na aba atual.
- O sistema aceita variações de nomes de agentes para garantir robustez.

### Contexto Compartilhado
- O objeto `MCP` armazena o contexto compartilhado entre os agentes, permitindo memória e contexto global.

## Fluxo Resumido
1. Usuário seleciona um agente e envia uma mensagem.
2. Mensagem é registrada no histórico do agente.
3. O agente (ou o orquestrador Anakin) processa a mensagem usando LLM.
4. O prefixo da resposta é analisado para identificar o agente que respondeu.
5. O histórico e a aba são atualizados conforme o agente que respondeu.
6. O usuário vê a resposta e pode continuar a conversa, inclusive mudando de agente automaticamente.

## Pontos de Destaque
- **Multiagente real**: Cada agente pode ser especializado (ex: C3PO para respostas técnicas, R2D2 para respostas curtas, Anakin como orquestrador).
- **LLM como cérebro**: Todas as respostas são geradas por LLM, tornando o sistema flexível e inteligente.
- **Interface fluida**: Troca automática de agente, histórico separado, visual moderno.
- **Segurança**: Uso de `.env` para chaves de API.
- **Extensível**: Fácil adicionar novos agentes ou especializações.

## Como Executar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Crie um arquivo `.env` com sua chave da API Gemini:
   ```env
   GEMINI_API_KEY=seu_token_aqui
   ```
3. Execute a aplicação:
   ```bash
   streamlit run app/main.py
   ```

## Possíveis Extensões
- Adicionar novos agentes com personalidades diferentes.
- Integrar outros modelos LLM.
- Salvar e carregar históricos de conversas.
- Adicionar comandos especiais ou integração com APIs externas.

## Detalhes Técnicos Adicionais

### O que é o ADK (Agent Development Kit)?
O ADK neste projeto é um conjunto de utilitários e padrões para facilitar a criação, orquestração e integração de múltiplos agentes inteligentes. Ele permite que cada agente tenha sua própria lógica, mas compartilhe contexto e recursos de forma padronizada.

- **src/agents/**: Cada arquivo representa um agente. Por exemplo, `anakin.py` implementa o agente orquestrador, enquanto `c3po.py` e `r2d2.py` implementam agentes especializados.

### Como funciona o MCP (Model Context Protocol)?
O MCP é responsável por:
- Armazenar o histórico global da conversa.
- Permitir que agentes acessem informações compartilhadas (ex: nome do usuário, tópicos já discutidos, decisões anteriores).
- Facilitar a passagem de contexto entre agentes, tornando a conversa mais natural e "lembrando" de fatos importantes.

- **src/adk/mcp.py**: Implementa o MCP (Model Context Protocol), que é o "cérebro coletivo" dos agentes. Ele armazena informações relevantes da conversa, contexto global, e permite que os agentes consultem e atualizem esse contexto.

#### Exemplo de uso do MCP no código:
```python
from src.adk.mcp import MCP

# Inicialização
if 'mcp' not in st.session_state:
    st.session_state.mcp = MCP()

# Ao chamar um agente:
response = agent_obj.run(msg, st.session_state.mcp.get_all())
```
- O método `get_all()` retorna todo o contexto armazenado, que pode ser usado pelo agente para gerar respostas mais inteligentes.

### Exemplo de lógica de um agente (simplificado):
```python
class C3POAgent:
    def run(self, mensagem, contexto):
        # Usa o contexto para responder de forma mais relevante
        if 'idioma' in contexto:
            # Responde no idioma preferido
            ...
        # Gera resposta usando LLM
        resposta = gerar_resposta_llm(mensagem, contexto)
        return f"C3PO: {resposta}"
```

### Orquestração entre agentes
- O Anakin funciona como "dispatcher". Ele pode decidir, com base na mensagem do usuário e no contexto, qual agente deve responder.
- O MCP garante que todos os agentes tenham acesso ao mesmo contexto, permitindo decisões mais inteligentes e colaborativas.

### Vantagens do uso do ADK/MCP
- **Escalabilidade**: Fácil adicionar novos agentes ou especializações.
- **Memória compartilhada**: Conversas mais naturais, pois os agentes "lembram" do que já foi dito.
- **Orquestração flexível**: O agente orquestrador pode delegar tarefas, repassar mensagens e até combinar respostas de múltiplos agentes.

## Sobre o MCP (Model Context Protocol)

O MCP (Model Context Protocol) é um componente central da arquitetura deste projeto. Ele funciona como uma "memória compartilhada" entre todos os agentes, permitindo que cada agente acesse, armazene e compartilhe informações relevantes do contexto da conversa.

### Principais funções do MCP:
- **Armazenamento de contexto global**: Guarda informações importantes, como histórico de mensagens, preferências do usuário, tópicos discutidos e decisões tomadas.
- **Acesso padronizado ao contexto**: Todos os agentes interagem com o MCP por meio de métodos padronizados, como `get_all()`, `set(key, value)`, `get(key)`, etc.
- **Facilita a colaboração entre agentes**: Como todos os agentes acessam o mesmo contexto, eles podem colaborar, repassar informações e construir respostas mais inteligentes e coesas.

### Exemplo de uso do MCP no código:
```python
from src.adk.mcp import MCP

# Inicialização do MCP na sessão do Streamlit
if 'mcp' not in st.session_state:
    st.session_state.mcp = MCP()

# Ao chamar um agente, passa-se o contexto global:
response = agent_obj.run(msg, st.session_state.mcp.get_all())

# Dentro do agente, é possível acessar e modificar o contexto:
class C3POAgent:
    def run(self, mensagem, contexto):
        idioma = contexto.get('idioma', 'pt-br')
        # ... lógica ...
        # Atualizando o contexto global
        contexto['ultimo_agente'] = 'C3PO'
        return f"C3PO: {resposta}"
```

### Benefícios do MCP
- **Memória persistente durante a sessão**: O MCP garante que informações importantes não se percam entre as interações.
- **Conversas mais naturais**: Os agentes podem "lembrar" do que já foi dito, tornando as respostas mais relevantes.
- **Base para extensões**: Novos agentes ou funcionalidades podem ser facilmente integrados ao sistema, aproveitando o contexto global já existente.

> O MCP é um diferencial do projeto, pois permite que múltiplos agentes atuem de forma coordenada, colaborativa e contextualizada, elevando o nível de inteligência e naturalidade das interações.

## Arquitetura Detalhada do Projeto

### 1. Visão Geral
O projeto segue uma arquitetura orientada a agentes, onde cada agente é uma entidade autônoma capaz de processar mensagens, acessar contexto compartilhado e interagir com outros agentes. A interface web (Streamlit) serve como ponto de entrada para o usuário, enquanto o ADK (Agent Development Kit) e o MCP (Model Context Protocol) fornecem a base para comunicação, memória e orquestração entre agentes.

### 2. Componentes Principais

#### a) Interface (Frontend)
- **Streamlit**: Responsável por toda a interação com o usuário. Exibe o chat, histórico, imagens dos agentes e permite o envio de mensagens.
- **Controle de Agente Ativo**: O usuário escolhe o agente com quem quer interagir, e a interface troca automaticamente para o agente que respondeu.

#### b) Núcleo de Agentes (Backend)
- **Agentes**: Cada agente é uma classe Python independente, com sua própria lógica de resposta. Exemplos:
  - `AnakinAgent`: Orquestrador, pode decidir qual agente deve responder.
  - `C3POAgent`, `R2D2Agent`: Agentes especializados, com personalidades e estilos próprios.
- **Orquestração**: O Anakin pode atuar como dispatcher, roteando mensagens para outros agentes conforme o contexto.

#### c) ADK (Agent Development Kit)
- Fornece padrões e utilitários para criação e integração de agentes.
- Garante que todos os agentes sigam uma interface comum (ex: método `run(mensagem, contexto)`).

#### d) MCP (Model Context Protocol)
- Atua como "memória compartilhada" entre todos os agentes.
- Permite que agentes acessem e atualizem informações globais da conversa.
- Facilita a passagem de contexto, tornando a experiência mais coesa e inteligente.

#### e) LLM (Large Language Model)
- Todos os agentes usam um modelo LLM (via Google Gemini) para gerar respostas naturais e contextuais.
- O LLM pode ser chamado diretamente pelo agente ou via Anakin (orquestrador).

### 3. Fluxo de Dados
1. **Usuário envia mensagem** pela interface Streamlit.
2. **Mensagem é registrada** no histórico do agente selecionado.
3. **Agente é chamado** (diretamente ou via Anakin) para processar a mensagem.
4. **Agente acessa o contexto** via MCP, podendo usar informações globais para enriquecer a resposta.
5. **Resposta é gerada** pelo LLM, possivelmente com um prefixo indicando o agente que respondeu.
6. **Sistema detecta o agente** na resposta e atualiza o histórico e a interface para o agente correto.
7. **Usuário visualiza a resposta** e pode continuar a conversa, inclusive mudando de agente automaticamente.

### 4. Vantagens da Arquitetura
- **Modularidade**: Fácil adicionar, remover ou modificar agentes sem impactar o sistema como um todo.
- **Escalabilidade**: Suporte a múltiplos agentes, cada um com lógica e personalidade próprias.
- **Memória Compartilhada**: O MCP permite que todos os agentes "lembrem" do contexto global, tornando as interações mais naturais.
- **Orquestração Inteligente**: O Anakin pode delegar tarefas, combinar respostas ou repassar mensagens entre agentes.
- **Extensibilidade**: Possível integrar novos modelos LLM, comandos especiais, ou até agentes externos.

### 5. Exemplo Visual da Arquitetura

```
[Usuário] ⇄ [Streamlit UI] ⇄ [Agente Selecionado]
                                 ↓
                        [ADK / MCP Contexto]
                                 ↓
                        [LLM (Gemini API)]
                                 ↓
                [Outros Agentes via Orquestração]
```

- O usuário interage com a interface.
- A interface chama o agente selecionado.
- O agente acessa o contexto global (MCP) e pode acionar outros agentes.
- O LLM gera a resposta, que é exibida ao usuário.

---

## Diagrama da Arquitetura

```mermaid
graph TD
    A[Usuário] <--> B[Streamlit UI]
    B --> C[Agente Selecionado]
    C --> D[ADK / MCP Contexto]
    D --> E[LLM (Gemini API)]
    C <--> F[Outros Agentes via Orquestração]
```

- O usuário interage com a interface web.
- A interface chama o agente selecionado.
- O agente acessa o contexto global (MCP) e pode acionar outros agentes.
- O LLM gera a resposta, que é exibida ao usuário.

---

## Exemplos de Código de Cada Camada

### 1. Interface (Streamlit UI)
```python
# app/main.py
import streamlit as st
from src.agents.anakin import AnakinAgent
from src.adk.mcp import MCP

if 'mcp' not in st.session_state:
    st.session_state.mcp = MCP()

# Seleção do agente
selected_agent = st.radio("Escolha o agente:", ["Anakin", "C3PO", "R2D2"])

# Envio de mensagem
msg = st.text_input("Mensagem:")
if st.button("Enviar"):
    response = st.session_state.agent.run(msg, st.session_state.mcp.get_all())
    st.write(response)
```

### 2. Agente (Backend)
```python
# src/agents/c3po.py
class C3POAgent:
    def run(self, mensagem, contexto):
        idioma = contexto.get('idioma', 'pt-br')
        resposta = gerar_resposta_llm(mensagem, contexto)
        contexto['ultimo_agente'] = 'C3PO'
        return f"C3PO: {resposta}"
```

### 3. MCP (Model Context Protocol)
```python
# src/adk/mcp.py
class MCP:
    def __init__(self):
        self.contexto = {}
    def get_all(self):
        return self.contexto
    def set(self, key, value):
        self.contexto[key] = value
    def get(self, key, default=None):
        return self.contexto.get(key, default)
```

### 4. LLM (Gemini API)
```python
import google.generativeai as genai

def gerar_resposta_llm(mensagem, contexto):
    # Exemplo simplificado
    resposta = genai.generate_content(mensagem)
    return resposta.text
```

---

## Detalhes sobre Extensões

- **Adicionar novos agentes**: Basta criar uma nova classe em `src/agents/` seguindo o padrão do método `run(mensagem, contexto)`.
- **Integrar outros modelos LLM**: Implemente uma função similar a `gerar_resposta_llm` usando a API desejada e altere os agentes para usá-la.
- **Salvar/carregar históricos**: Implemente métodos no MCP para persistir o contexto em arquivos ou banco de dados.
- **Comandos especiais**: Adicione lógica nos agentes para reconhecer e executar comandos específicos (ex: `/ajuda`, `/reset`).
- **Integração com APIs externas**: Os agentes podem consumir APIs externas e compartilhar resultados via MCP.

---
