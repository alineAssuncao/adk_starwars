from abc import ABC, abstractmethod

class Agent(ABC):
    """
    Base class for all agents in the system.
    """
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self, user_input: str, context: dict) -> str:
        """
        Run the agent's logic.

        :param user_input: The input from the user.
        :param context: The shared context between agents.
        :return: The agent's response.
        """
        pass
