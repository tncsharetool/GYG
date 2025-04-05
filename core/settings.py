# core/settings.py

import os

def app_settings():
    return {
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY", ""),
        "FIREBASE_API_KEY": os.getenv("FIREBASE_API_KEY", ""),
        "GEMINI_API_KEY": os.getenv("GEMINI_API_KEY", ""),
        "LANG": os.getenv("LANG", "vi")
    }
# settings.py content here
