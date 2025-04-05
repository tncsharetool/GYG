# core/ui/theme_switcher.py

import streamlit as st

def switch_theme():
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = True
    dark = st.checkbox("🌙 Dark Mode", value=st.session_state.dark_mode)
    st.session_state.dark_mode = dark
