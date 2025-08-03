
import os
from src.adk.agent import Agent
from src.agents.c3po import C3POAgent
from src.agents.r2d2 import R2D2Agent
try:
    import google.generativeai as genai
except ImportError:
    genai = None

class AnakinAgent(Agent):
    """
    Anakin agent for orchestrating the other agents.
    """
    def __init__(self):
        super().__init__("Anakin")
        self.c3po = C3POAgent()
        self.r2d2 = R2D2Agent()

    def run(self, user_input: str, context: dict) -> str:
        """
        Run Anakin's logic: always use Gemini LLM as orchestrator, letting it decidir qual agente responde ou se responde como Anakin.
        """
        api_key = os.getenv("GEMINI_API_KEY")
        if genai and api_key:
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-2.0-flash')
                system_prompt = (
                    "Você é Anakin, o orquestrador dos agentes Star Wars. "
                    "Os agentes disponíveis são: C3PO (formal e analítico) e R2D2 (técnico e objetivo). "
                    "Analise a mensagem do usuário e decida: "
                    "- Se for um pedido formal, de risco ou protocolo, faça a chamada ao agente C3PO.\n"
                    "- Se for técnico, de dados ou código, faça a chamada ao agente R2D2.\n"
                    "- Se for pessoal, emocional ou não se encaixar nos outros, responda como Anakin.\n"
                    "- Se o usuário pedir para falar com um agente específico, responda com esse agente.\n"
                    "Faça com que o agente que está respondendo escreva o nome do agente que está respondendo (Ex: 'C3PO: ...', 'R2D2: ...', 'Anakin: ...')."
                )
                prompt = f"Mensagem do usuário: {user_input}\nContexto: {context}"
                response = model.generate_content([system_prompt, prompt])
                if hasattr(response, 'text'):
                    return response.text
                elif hasattr(response, 'candidates') and response.candidates:
                    return response.candidates[0].text
                else:
                    return str(response)
            except Exception as e:
                return f"[Anakin] Erro ao acessar Gemini: {e}"
        return "[Anakin] Não foi possível acessar a LLM."
