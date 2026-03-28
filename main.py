from core.orchestrator.main import Orchestrator
from agents.process_orchestration.invoice_agent import InvoiceAgent


def run_demo():
    print("\n🚀 Starting ARIA Demo...\n")

    # Initialize system
    orchestrator = Orchestrator()
    agent = InvoiceAgent("InvoiceAgent")

    # Intentionally broken input (to trigger self-healing)
    invoice_data = {
        "vendor": "ABC Corp",
        "amount": 5000,
        "po_number": None
    }

    print("📥 Input Invoice:", invoice_data)

    # Execute workflow
    result = orchestrator.execute(agent, invoice_data)

    print("\n✅ FINAL RESULT:")
    print(result)

    print("\n📊 Demo Complete\n")


if __name__ == "__main__":
    run_demo()