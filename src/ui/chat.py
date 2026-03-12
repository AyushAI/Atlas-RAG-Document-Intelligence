import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

def render_chat_interface():
    st.header("💬 Chat Workspace")
    
    # Display message history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    
    # Chat Input
    if user_input := st.chat_input("Ask a question about your documents..."):
        # Add user message
        st.session_state.messages.append({"role":"user","content":user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
            
        # Get response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            with st.spinner("Analyzing documents..."):
                payload = {
                    "question": user_input,
                    "username": st.session_state.username,
                    "model": st.session_state.get("selected_model", "models/gemini-3-flash-preview")
                }

                try:
                    res = requests.post(f"{BACKEND_URL}/chat", json=payload)
                    
                    if res.status_code == 200:
                        answer = res.json()["answer"]
                    else:
                        answer = f"⚠️ Error: {res.text}"
                except Exception as e:
                    answer = f"🔌 Connection error: {e}"
                
                message_placeholder.markdown(answer)
                st.session_state.messages.append({"role":"assistant","content":answer})
