class MCP:
    """
    Model Context Protocol (MCP) for sharing context between agents.
    """
    def __init__(self):
        self._context = {}

    def set(self, key: str, value: any):
        """
        Set a value in the shared context.
        """
        self._context[key] = value

    def get(self, key: str) -> any:
        """
        Get a value from the shared context.
        """
        return self._context.get(key)

    def get_all(self) -> dict:
        """
        Get the entire context dictionary.
        """
        return self._context.copy()
