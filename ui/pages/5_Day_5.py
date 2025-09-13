import streamlit as st
from utils import post_json

st.set_page_config(page_title="Day 5 - Open Agent", page_icon="🔎")

st.title("Day 5 · Open Matching/Search Agent (chat)")

if "messages_d5" not in st.session_state:
    st.session_state.messages_d5 = []

for msg in st.session_state.messages_d5:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Describe your expert search or query"):
    st.session_state.messages_d5.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.spinner("Searching..."):
        payload = {"messages": st.session_state.messages_d5}
        data = post_json("/api/day5/chat", payload)
    reply = data.get("reply", "<no reply>")
    st.session_state.messages_d5.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
