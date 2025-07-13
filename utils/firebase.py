import firebase_admin
from firebase_admin import credentials, firestore
import streamlit as st

# Convert SecretsDict to regular dict
firebase_dict = dict(st.secrets["firebase"])

# Initialize Firebase only once
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_dict)
    firebase_admin.initialize_app(cred)

db = firestore.client()
