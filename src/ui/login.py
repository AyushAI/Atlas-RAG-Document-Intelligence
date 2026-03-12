import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

def render_login_page():
    # Centered layout using columns
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<h1 style='text-align: center; color: #4a90e2;'>RAG Chatbot</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #aaa;'>Secure & Intelligent Document Assistant</p>", unsafe_allow_html=True)
        st.write("") # Spacer
        
        tab1, tab2 = st.tabs(["🔒 Login", "📝 Register"])
        
        with tab1:
            st.subheader("Welcome Back")
            username_login = st.text_input("Username", key="login_user", placeholder="Enter your username")
            password_login = st.text_input("Password", type="password", key="login_pass", placeholder="Enter your password")
            st.write("")
            
            if st.button("Log In", use_container_width=True):
                if username_login and password_login:
                    try:
                        res = requests.post(f"{BACKEND_URL}/login", json={"username": username_login, "password": password_login})
                        if res.status_code == 200:
                            data = res.json()
                            st.session_state.username = username_login
                            # Restore message history if available
                            if "history" in data:
                                st.session_state.messages = data["history"]
                            st.success("Login successful!")
                            st.rerun()

                        else:
                            st.error(res.json().get("detail", "Login failed"))
                    except Exception as e:
                        st.error(f"Connection Error: {e}")
                else:
                    st.warning("Please fill in all fields")

        with tab2:
            st.subheader("Create Account")
            username_reg = st.text_input("Username", key="reg_user", placeholder="Choose a username")
            password_reg = st.text_input("Password", type="password", key="reg_pass", placeholder="Choose a password")
            st.write("")
            
            if st.button("Sign Up", use_container_width=True):
                if username_reg and password_reg:
                    try:
                        res = requests.post(f"{BACKEND_URL}/register", json={"username": username_reg, "password": password_reg})
                        if res.status_code == 200:
                            st.success("Registration successful! Please proceed to Login.")
                        else:
                            st.error(res.json().get("detail", "Registration failed"))
                    except Exception as e:
                        st.error(f"Connection Error: {e}")
                else:
                    st.warning("Please fill in all fields")
