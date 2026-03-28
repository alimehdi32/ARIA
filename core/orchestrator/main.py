from core.retry_policy import RetryEngine
from audit.logger import AuditLogger
from agents.process_orchestration.verifier_agent import VerifierAgent


class Orchestrator:
    def __init__(self):
        self.retry_engine = RetryEngine()
        self.audit = AuditLogger()

    def execute(self, agent, data):
        self.audit.log(agent.name, "START", data)

        try:
            result = agent.run(data)
            self.audit.log(agent.name, "SUCCESS", result)
            return result

        except Exception as e:
            self.audit.log(agent.name, "FAILURE", str(e))

            print("[Orchestrator] Handling failure...")

            retry_result = self.retry_engine.handle(agent, data, e)

            self.audit.log(agent.name, "RECOVERY_SUCCESS", retry_result)
            
        verifier = VerifierAgent("VerifierAgent")
        verification = verifier.run(retry_result)

        self.audit.log("VerifierAgent", "VERIFICATION", verification)

        # Confidence check
        if retry_result["confidence"] < 0.6:
            print("[Orchestrator] Low confidence → Escalation needed")
            retry_result["status"] = "ESCALATED"

        return retry_result