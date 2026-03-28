from core.base_agent import BaseAgent


class VerifierAgent(BaseAgent):
    def think(self, data):
        output = data.get("output", "")

        # Simple validation logic (can be upgraded later)
        if "Invoice processed" in output:
            return "VALID"
        else:
            return "INVALID"