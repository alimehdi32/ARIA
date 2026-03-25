from core.orchestrator.main import Orchestrator
from agents.process_orchestration.invoice_agent import InvoiceAgent


def run_demo():
    orchestrator = Orchestrator()
    agent = InvoiceAgent("InvoiceAgent")

    # Broken input (intentional)
    invoice_data = {
        "vendor": "ABC Corp",
        "amount": 5000,
        "po_number": None
    }

    result = orchestrator.execute(agent, invoice_data)

    print("\nFINAL RESULT:")
    print(result)


if __name__ == "__main__":
    run_demo()