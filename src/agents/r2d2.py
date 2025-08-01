from src.adk.agent import Agent

class R2D2Agent(Agent):
    """
    R2D2 agent for technical and concise responses.
    """
    def __init__(self):
        super().__init__("R2D2")

    def run(self, user_input: str, context: dict) -> str:
        """
        Run R2D2's logic.
        """
        # In a real implementation, this would use an LLM to generate a response.
        # For now, we'll use a canned response.
        return "Beep boop beep... (I have analyzed the data and the probability of success is 99.7%)"
