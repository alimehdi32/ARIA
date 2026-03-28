from core.base_agent import BaseAgent


class InvoiceAgent(BaseAgent):
    def think(self, data):
        if not data.get("po_number"):
            raise Exception("Missing PO Number")

        return f"Invoice processed for {data['vendor']} amount {data['amount']}"