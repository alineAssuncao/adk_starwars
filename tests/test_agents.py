import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.agents.c3po import C3POAgent
from src.agents.r2d2 import R2D2Agent
from src.agents.anakin import AnakinAgent
from src.adk.mcp import MCP

class TestAgents(unittest.TestCase):

    def setUp(self):
        self.c3po = C3POAgent()
        self.r2d2 = R2D2Agent()
        self.anakin = AnakinAgent()
        self.mcp = MCP()

    def test_c3po_response(self):
        response = self.c3po.run("", self.mcp.get_all())
        self.assertIn("C-3PO", response)

    def test_r2d2_response(self):
        response = self.r2d2.run("", self.mcp.get_all())
        self.assertIn("Beep boop", response)

    def test_anakin_default_response(self):
        response = self.anakin.run("Hello there", self.mcp.get_all())
        self.assertIn("I'll handle this myself", response)

    def test_anakin_routes_to_c3po(self):
        response = self.anakin.run("What is the risk?", self.mcp.get_all())
        self.assertIn("C-3PO", response)

    def test_anakin_routes_to_r2d2(self):
        response = self.anakin.run("Give me the technical data.", self.mcp.get_all())
        self.assertIn("Beep boop", response)

if __name__ == '__main__':
    unittest.main()
