import streamlit as st
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.agents.anakin import AnakinAgent
from src.adk.mcp import MCP

def main():
    st.title("Star Wars Multi-Agent System")

    # Initialize the agent and context
    if 'agent' not in st.session_state:
        st.session_state.agent = AnakinAgent()
    if 'mcp' not in st.session_state:
        st.session_state.mcp = MCP()

    # Get user input
    user_input = st.text_input("You:", "What is the risk of an asteroid field?")

    if st.button("Send"):
        if user_input:
            # Run the orchestrator agent
            response = st.session_state.agent.run(user_input, st.session_state.mcp.get_all())
            st.session_state.mcp.set("last_response", response)

            # Display the response
            st.text_area("Agent Response:", value=response, height=200)
        else:
            st.warning("Please enter a message.")

if __name__ == "__main__":
    main()
