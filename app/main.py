
# Importações principais
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import sys
import os

# Adiciona o diretório src ao path do Python para facilitar imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.agents.anakin import AnakinAgent
from src.adk.mcp import MCP

def main():

    st.title("Star Wars Multi-Agent System")

    # Dicionário com os agentes e o caminho das imagens de cada um
    agents = {
        "Anakin": {
            "obj": AnakinAgent(),
            "img": "app/images/anakin.png"
        },
        "C3PO": {
            "img": "app/images/c3po.png"
        },
        "R2D2": {
            "img": "app/images/r2d2.png"
        }
    }

    # Inicializa o histórico de mensagens para cada agente, se ainda não existir
    for agent in agents:
        if f"history_{agent}" not in st.session_state:
            st.session_state[f"history_{agent}"] = []

    # Controle da "aba" ativa (0: Anakin, 1: C3PO, 2: R2D2)
    tab_labels = ["Anakin", "C3PO", "R2D2"]
    if 'active_tab' not in st.session_state:
        st.session_state.active_tab = 0
    selected_tab = st.radio(
        "Escolha o agente:",
        tab_labels,
        index=st.session_state.active_tab,
        key="tab_radio",
        horizontal=True
    )
    tab_map = {name: i for i, name in enumerate(tab_labels)}

    # Função para exibir o chat de cada agente
    def chat_tab(agent_name, agent_obj=None):
        # Exibe a imagem e o nome do agente
        st.image(agents[agent_name]["img"], width=100)
        st.markdown(f"### {agent_name}")
        # Exibe o histórico de mensagens do agente
        # Exibe o histórico de mensagens do agente
        history = st.session_state[f"history_{agent_name}"]
        for msg, sender in history:
            if sender == "user":
                st.markdown(f"""
                <div style='display: flex; justify-content: flex-end; margin-bottom: 8px;'>
                    <div style='background: #DCF8C6; color: #222; padding: 10px 16px; border-radius: 18px 18px 2px 18px; max-width: 70%; text-align: right;'>
                        <b>Você:</b> {msg}
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style='display: flex; justify-content: flex-start; margin-bottom: 8px;'>
                    <div style='background: #F1F0F0; color: #222; padding: 10px 16px; border-radius: 18px 18px 18px 2px; max-width: 70%; text-align: left;'>
                        <b>{agent_name}:</b> {msg}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        # Campo de input para enviar mensagem ao agente, usando formulário para permitir Enter
        # Estado para controlar o input do usuário
        form_key = f"form_{agent_name}"
        with st.form(key=form_key, clear_on_submit=True):
            user_input = st.text_input(f"Mensagem para {agent_name}")
            submitted = st.form_submit_button(f"Enviar para {agent_name}")
            if submitted:
                msg = user_input.strip()
                if msg:
                    st.session_state[f"history_{agent_name}"].append((msg, "user"))
                    if agent_obj:
                        response = agent_obj.run(msg, st.session_state.mcp.get_all())
                    else:
                        response = st.session_state.agent.run(f"falar com o {agent_name.lower()}: {msg}", st.session_state.mcp.get_all())
                    agent_detected = agent_name
                    if ":" in response:
                        agent_detected, response = response.split(":", 1)
                        agent_detected = agent_detected.strip().upper()
                        response = response.strip()
                    # Normaliza o nome do agente detectado para as chaves do dicionário
                    agent_detected_key = agent_detected.strip().upper().replace("-", "").replace(" ", "")
                    # Mapeamento robusto para possíveis variações
                    agent_aliases = {
                        "ANAKIN": "ANAKIN",
                        "C3PO": "C3PO",
                        "C3PO": "C3PO",
                        "C3-PO": "C3PO",
                        "C3 PO": "C3PO",
                        "R2D2": "R2D2",
                        "R2-D2": "R2D2",
                        "R2 D2": "R2D2"
                    }
                    # Tenta mapear para o nome correto
                    agent_detected_key = agent_aliases.get(agent_detected_key, agent_detected_key)
                    agent_tab_map = {"ANAKIN": 0, "C3PO": 1, "R2D2": 2}
                    agent_history_map = {"ANAKIN": "Anakin", "C3PO": "C3PO", "R2D2": "R2D2"}
                    # Permite troca de aba para todos os agentes
                    if agent_detected_key in agent_tab_map:
                        st.session_state[f"history_{agent_history_map[agent_detected_key]}"].append((response, "agent"))
                        st.session_state.active_tab = agent_tab_map[agent_detected_key]
                    else:
                        st.session_state[f"history_{agent_name}"].append((response, "agent"))
                    st.rerun()
                else:
                    st.warning("Digite uma mensagem.")

    # Inicializa o agente principal (Anakin) e o contexto MCP
    if 'agent' not in st.session_state:
        st.session_state.agent = agents["Anakin"]["obj"]
    if 'mcp' not in st.session_state:
        st.session_state.mcp = MCP()

    # Renderiza o chat do agente selecionado
    if selected_tab == "Anakin":
        chat_tab("Anakin", agent_obj=st.session_state.agent)
    elif selected_tab == "C3PO":
        chat_tab("C3PO")
    elif selected_tab == "R2D2":
        chat_tab("R2D2")

if __name__ == "__main__":
    main()
