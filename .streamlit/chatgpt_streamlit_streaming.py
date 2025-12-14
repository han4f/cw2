import streamlit as st
import time

st.title("💬 ChatGPT - Simulated Streaming")

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Say something...")
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role":"user","content":prompt})
    
    # Simulate streaming
    with st.chat_message("assistant"):
        container = st.empty()
        simulated_reply = f"[Simulated Streaming Response for: '{prompt}']"
        display_text = ""
        for char in simulated_reply:
            display_text += char
            container.markdown(display_text + "▌")
            time.sleep(0.02)
        container.markdown(display_text)
    
    st.session_state.messages.append({"role":"assistant","content":simulated_reply})
