import streamlit as st
from utils import post_json

st.set_page_config(page_title="Day 3 - Basic RAG", page_icon="📄")

st.title("Day 3 · Basic RAG (chat)")

if "messages_d3" not in st.session_state:
    st.session_state.messages_d3 = []

for msg in st.session_state.messages_d3:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask about the Tesla manual"):
    st.session_state.messages_d3.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.spinner("Retrieving..."):
        payload = {"messages": st.session_state.messages_d3}
        data = post_json("/api/day3/chat", payload)
    reply = data.get("reply", "<no reply>")
    st.session_state.messages_d3.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
