
import os
from src.adk.agent import Agent
try:
    import google.generativeai as genai
except ImportError:
    genai = None

class C3POAgent(Agent):
    """
    C3PO agent for formal and analytical responses.
    """
    def __init__(self):
        super().__init__("C3PO")

    def run(self, user_input: str, context: dict) -> str:
        """
        Run C3PO's logic. Uses Gemini LLM if available, else falls back to canned response.
        """
        api_key = os.getenv("GEMINI_API_KEY")
        if genai and api_key:
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-2.0-flash')
                response = model.generate_content(f"Responda de forma formal e analítica como C-3PO: {user_input}")
                if hasattr(response, 'text'):
                    return response.text
                elif hasattr(response, 'candidates') and response.candidates:
                    return response.candidates[0].text
                else:
                    return str(response)
            except Exception as e:
                return f"[C3PO] Erro ao acessar Gemini: {e}"
        return "Saudações. Eu sou C-3PO, relações humano-ciborgue. Como posso ajudar?"
