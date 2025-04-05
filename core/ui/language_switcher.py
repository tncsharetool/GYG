# core/ui/language_switcher.py

import streamlit as st

def switch_language():
    st.markdown("🌍 **Language**")
    st.selectbox("Language", options=["vi", "en"], index=0, key="lang")
