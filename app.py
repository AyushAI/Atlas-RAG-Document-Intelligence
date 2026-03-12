import streamlit as st
from src.ui.styles import apply_custom_styles
from src.ui.login import render_login_page
from src.ui.sidebar import render_sidebar
from src.ui.chat import render_chat_interface

# Page Config
st.set_page_config(
    page_title="RAG Chatbot", 
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply Custom CSS
apply_custom_styles()

def main():
    # Session Initialization
    if "username" not in st.session_state:
        st.session_state.username = None
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "selected_model" not in st.session_state:
        st.session_state.selected_model = "models/gemini-3-flash-preview"

    # Routing
    if not st.session_state.username:
        render_login_page()
    else:
        # Main App Layout
        selected_page = render_sidebar()

        
        if selected_page == "💬 Chat":
            render_chat_interface()
        elif selected_page == "📄 Documents":
            st.title("📄 Document Management")
            st.info("Use the sidebar to upload and summarize documents.")
            # We could move the upload UI here from sidebar if we wanted, 
            # but for now it's in the sidebar as per the module.
            # Let's show a placeholder or instructions here.
            st.markdown("""
            ### How to use:
            1.  **Upload**: Use the sidebar 'Documents' tab to upload files.
            2.  **Summarize**: Generate summaries of your uploaded files.
            3.  **Chat**: Switch to the 'Chat' tab to ask questions.
            """)
        elif selected_page == "🛠️ Tools":
            st.title("🛠️ Utilities")
            st.info("Additional tools available in the sidebar.")
            st.markdown("""
            -   **Text Summarizer**: Paste any text to get a quick summary.
            -   **Chat Summary**: Get a recap of your conversation so far.
            """)

if __name__ == "__main__":
    main()