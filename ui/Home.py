import streamlit as st

st.set_page_config(page_title="Summerschool 2025", page_icon="🎓")

st.title("Summerschool 2025 — Labs UI")

st.markdown("""
- Day 1 and Day 2 use a simple single-message input via `st.chat_input`.
- Days 3–5 use a full chat interface with `st.chat_message` + `st.chat_input`.

Use the sidebar to switch between pages (files under `ui/pages/`).
""")
