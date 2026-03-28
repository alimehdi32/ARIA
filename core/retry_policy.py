class FailureClassifier:
    def classify(self, error):
        msg = str(error).lower()

        if "timeout" in msg:
            return "TRANSIENT"
        elif "missing" in msg:
            return "DATA_ERROR"
        else:
            return "UNKNOWN"


class RetryEngine:
    def __init__(self):
        # ✅ THIS LINE IS CRITICAL
        self.classifier = FailureClassifier()

    def handle(self, agent, data, error):
        category = self.classifier.classify(error)

        print(f"[RetryEngine] Failure type: {category}")

        if category == "TRANSIENT":
            print("[Retry] Retrying...")
            return agent.run(data)

        elif category == "DATA_ERROR":
            print("[Retry] Fixing data...")
            data["po_number"] = "AUTO-PO-123"
            return agent.run(data)

        else:
            raise error