from src.adk.agent import Agent
from src.agents.c3po import C3POAgent
from src.agents.r2d2 import R2D2Agent

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
        Run Anakin's logic, routing to the appropriate agent.
        """
        user_input_lower = user_input.lower()
        if any(keyword in user_input_lower for keyword in ["risk", "danger", "formal"]):
            return self.c3po.run(user_input, context)
        elif any(keyword in user_input_lower for keyword in ["technical", "data", "code"]):
            return self.r2d2.run(user_input, context)
        else:
            return "I'll handle this myself. What's the situation?"
