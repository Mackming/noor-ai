from utils.firebase import db
from datetime import datetime

def log_event(event_type, details, page=None, user_context=None):
    """
    Logs an event to Firestore.
    
    Args:
        event_type (str): "info", "error", "warning", etc.
        details (str): Description of the event or error.
        page (str): Optional - Which page the event occurred on.
        user_context (dict): Optional - Details about the user (gender, addiction, etc.)
    """

    log_data = {
        "event_type": event_type,
        "details": details,
        "page": page,
        "user_context": user_context if user_context else {},
        "timestamp": datetime.utcnow()
    }

    try:
        db.collection("logs").add(log_data)
        print("✅ Log saved to Firebase.")
    except Exception as e:
        print("❌ Failed to log to Firebase:", e)
