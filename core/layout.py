# core/layout.py

import streamlit as st
from dotenv import load_dotenv
import os

from core.ui.theme_switcher import switch_theme
from core.ui.language_switcher import switch_language
from core.ui.user_avatar import show_user_avatar
from core.ui.prompt_suggestions import show_prompt_suggestions
from core.ui.footer import show_footer

from core.firebase_login import show_login
from core.settings import app_settings
from core.langs import set_language

load_dotenv()

def main():
    st.set_page_config(
        page_title="VN AI Travel Planner",
        page_icon="🧭",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Sidebar UI
    with st.sidebar:
        switch_theme()
        switch_language()
        show_user_avatar()

    user = show_login()
    if user:
        set_language()
        st.title("🧳 VN Vietnam AI Travel")
        st.markdown("### ✨ Lên kế hoạch chuyến đi hoàn hảo với AI – Chỉ cần nhập mong muốn!")

        show_prompt_suggestions()

        prompt = st.text_area("✍️ Mô tả chuyến đi lý tưởng của bạn:")
        if st.button("⚡ Tạo lịch trình"):
            st.success("🗺️ Địa điểm nổi bật sẽ hiển thị ở đây (đang xử lý...)")

        show_footer()
    else:
        st.stop()
# layout.py content here
