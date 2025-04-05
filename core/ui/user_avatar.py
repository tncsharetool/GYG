# core/ui/user_avatar.py

import streamlit as st
from PIL import Image

def show_user_avatar():
    try:
        avatar = Image.open("assets/avatar_placeholder.jpg")
        st.sidebar.image(avatar, width=80, caption="Guest User")
    except:
        st.sidebar.write("🧑‍💻 Guest User")
