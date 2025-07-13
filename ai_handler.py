import google.generativeai as genai
import time
import random
import streamlit as st

GEMINI_KEYS = [
    {
        "key": st.secrets["gpt_keys"]["key1"],
        "models": ["gemini-2.5-flash-lite-preview-06-17", "gemini-2.0-flash-lite", "gemini-2.0-flash"]
    },
    {
        "key": st.secrets["gpt_keys"]["key2"],
        "models": ["gemini-2.5-flash-lite-preview-06-17", "gemini-2.0-flash-lite", "gemini-2.0-flash"]
    },
    {
        "key": st.secrets["gpt_keys"]["key3"],
        "models": ["gemini-2.5-flash-lite-preview-06-17", "gemini-2.0-flash-lite", "gemini-2.0-flash"]
    },
    {
        "key": st.secrets["gpt_keys"]["key4"],
        "models": ["gemini-2.5-flash-lite-preview-06-17", "gemini-2.0-flash-lite", "gemini-2.0-flash"]
    }
]

def generate_advice(prompt):
    for key_entry in GEMINI_KEYS:
        api_key = key_entry["key"]
        for model_name in key_entry["models"]:
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(prompt)
                if response and response.text:
                    return {
                        "model": model_name,
                        "response": response.text.strip()
                    }
            except Exception as e:
                print(f"⚠️ Failed with {model_name} on {api_key[:25]}... → {e}")
                time.sleep(random.uniform(0.5, 1.5))  # to avoid aggressive hitting
    return {
        "error": "❌ All models and API keys exhausted. Try again later."
    }
