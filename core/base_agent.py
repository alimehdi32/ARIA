from core.confidence import calculate_confidence


class AgentFailure(Exception):
    def __init__(self, agent_name, message):
        self.agent_name = agent_name
        self.message = message
        super().__init__(f"{agent_name} failed: {message}")


class BaseAgent:
    def __init__(self, name):
        self.name = name

    def run(self, input_data):
        try:
            output = self.think(input_data)
            confidence = calculate_confidence(output)

            return {
                "agent": self.name,
                "output": output,
                "confidence": confidence,
                "status": "SUCCESS"
            }

        except Exception as e:
            raise AgentFailure(self.name, str(e))

    def think(self, input_data):
        raise NotImplementedError