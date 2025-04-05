# core/langs.py

import os
import streamlit as st

def set_language():
    lang = os.getenv("LANG", "vi")
    st.session_state["lang"] = lang
# langs.py content here
