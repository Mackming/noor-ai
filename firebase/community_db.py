from firebase_admin import firestore
from datetime import datetime
from utils.firebase import db

db = firestore.client()
stories_ref = db.collection("approved_stories")


def get_approved_stories():
    
    docs = stories_ref.where("approved", "==", True).order_by("timestamp", direction=firestore.Query.DESCENDING).stream()
    return [(doc.id, doc.to_dict()) for doc in docs]


def delete_story(story_id):
    stories_ref.document(story_id).delete()
