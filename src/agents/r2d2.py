
import os
from src.adk.agent import Agent
try:
    import google.generativeai as genai
except ImportError:
    genai = None

class R2D2Agent(Agent):
    """
    R2D2 agent for technical and concise responses.
    """
    def __init__(self):
        super().__init__("R2D2")

    def run(self, user_input: str, context: dict) -> str:
        """
        Run R2D2's logic. Uses Gemini LLM if available, else falls back to canned response.
        """
        api_key = os.getenv("GEMINI_API_KEY")
        if genai and api_key:
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-2.0-flash')
                response = model.generate_content(user_input)
                if hasattr(response, 'text'):
                    return response.text
                elif hasattr(response, 'candidates') and response.candidates:
                    return response.candidates[0].text
                else:
                    return str(response)
            except Exception as e:
                return f"[R2D2] Erro ao acessar Gemini: {e}"
        # Fallback: resposta padrão multilíngue
        user_input_lower = user_input.lower()
        pt_keywords = ["dados", "técnico", "tecnico", "código", "codigo", "probabilidade"]
        if any(word in user_input_lower for word in pt_keywords):
            return "Bip boop bip... (Analisei os dados e a probabilidade de sucesso é 99,7%)"
        else:
            return "Beep boop beep... (I have analyzed the data and the probability of success is 99.7%)"
