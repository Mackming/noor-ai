import google.generativeai as genai
from utils.api_keys import GEMINI_KEYS
import time
import random

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
