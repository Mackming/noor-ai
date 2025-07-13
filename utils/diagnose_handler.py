from utils.firebase import db
from datetime import datetime

def calculate_severity(answers):
    """
    Very basic severity logic. Can be replaced by AI scoring later.
    """
    severity_score = 0

    frequency = answers.get("frequency", "").lower()
    if "daily" in frequency:
        severity_score += 3
    elif "week" in frequency:
        severity_score += 2
    else:
        severity_score += 1

    if answers.get("relapse") == "often":
        severity_score += 2
    elif answers.get("relapse") == "rarely":
        severity_score += 1

    return "High" if severity_score >= 5 else "Moderate" if severity_score >= 3 else "Low"

def save_diagnosis(answers):
    """
    Save the user's diagnostic answers to Firebase Firestore.
    """
    severity = calculate_severity(answers)

    data = {
        "age": answers.get("age"),
        "gender": answers.get("gender"),
        "province": answers.get("province"),
        "addiction": answers.get("addiction"),
        "frequency": answers.get("frequency"),
        "relapse": answers.get("relapse"),
        "started": answers.get("started"),
        "struggles": answers.get("struggles"),
        "severity": severity,
        "religious_mode": answers.get("religious_mode", False),
        "timestamp": datetime.utcnow()
    }

    try:
        db.collection("diagnostics").add(data)
        print("✅ Diagnosis saved successfully.")
        return severity
    except Exception as e:
        print("❌ Failed to save diagnosis:", e)
        return None
