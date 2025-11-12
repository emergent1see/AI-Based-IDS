class AlertEngine:
    def __init__(self):
        pass
    def raise_alert(self, rule_id, context):
        print("ALERT", rule_id, context)
