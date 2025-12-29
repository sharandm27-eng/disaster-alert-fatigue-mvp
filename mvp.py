# Disaster Alert System with Alert Fatigue Control
# PS-6 MVP (Console Based)

def calculate_risk(severity, area_risk):
    risk_map = {"low": 1, "medium": 2, "high": 3}
    return risk_map[severity] + risk_map[area_risk]

def calculate_fatigue(hours_since_last_alert):
    if hours_since_last_alert < 1:
        return "high"
    elif 1 <= hours_since_last_alert <= 4:
        return "medium"
    else:
        return "low"

def make_decision(risk_score, fatigue):
    if risk_score >= 5 and fatigue != "high":
        return "SEND"
    elif risk_score >= 3 and fatigue == "high":
        return "DELAY"
    else:
        return "SUPPRESS"

def explain(decision, risk_score, fatigue):
    return f"Decision is {decision} because risk score is {risk_score} and alert fatigue is {fatigue}."

# ---- Main Program ----
print("=== Disaster Alert System MVP ===")

severity = input("Enter disaster severity (low/medium/high): ").lower()
area_risk = input("Enter area risk (low/medium/high): ").lower()
hours = float(input("Enter hours since last alert: "))

risk_score = calculate_risk(severity, area_risk)
fatigue = calculate_fatigue(hours)
decision = make_decision(risk_score, fatigue)

explanation = explain(decision, risk_score, fatigue)

print("\n--- Alert Decision ---")
print("Decision:", decision)
print("Explanation:", explanation)
