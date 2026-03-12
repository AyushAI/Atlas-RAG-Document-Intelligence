import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

def render_sidebar():
    with st.sidebar:
        st.markdown(f"### 👋 Hi, {st.session_state.username}")
        
        # Model Selection
        st.markdown("---")
        st.header("⚙️ AI Configuration")
        
        model_options = {
            "🚀 Gemini 3 Flash": {
                "id": "models/gemini-3-flash-preview",
                "desc": "Next-gen speed & intelligence (Experimental)."
            },
            "⚡ Gemini 2.5 Flash": {
                "id": "models/gemini-2.5-flash",
                "desc": "Fast & efficient for high-volume tasks."
            },
            "🧠 Gemini 3 Pro": {
                "id": "models/gemini-3-pro-preview",
                "desc": "Advanced reasoning & complex understanding."
            },
            "🔋 Gemini 2.5 Flash Lite": {
                "id": "models/gemini-2.5-flash-lite",
                "desc": "Lightweight & cost-effective for simple tasks."
            }
        }
        
        selected_model_name = st.selectbox(
            "Select AI Model",
            options=list(model_options.keys()),
            help="Choose the model that best fits your needs."
        )
        
        st.session_state.selected_model = model_options[selected_model_name]["id"]
        st.caption(f"_{model_options[selected_model_name]['desc']}_")
        
        # Navigation

        selection = st.radio(
            "Navigation", 
            ["💬 Chat", "📄 Documents", "🛠️ Tools"],
            label_visibility="collapsed"
        )
        st.markdown("---")
        
        if selection == "💬 Chat":
            pass # Chat controls could go here
            
        elif selection == "📄 Documents":
            st.header("Upload Document")
            uploaded_file = st.file_uploader(
                "Drop files here",
                type=['pdf','txt', 'xlsx', 'xls', 'pptx', 'ppt', 'db', 'jpg', 'jpeg', 'png']
            )

            if uploaded_file:
                with st.spinner("Processing document..."):
                    files = {"file" : (uploaded_file.name, uploaded_file.getvalue())}
                    data = {"username": st.session_state.username}
                    
                    try:
                        response = requests.post(f"{BACKEND_URL}/upload", files=files, data=data)
                        if response.status_code == 200:
                            st.success("✅ Document processed!")
                        else:
                            st.error(f"❌ Error: {response.text}")
                    except Exception as e:
                        st.error(f"Connection error: {e}")
                        
            st.header("Summarize Document")
            doc_style = st.selectbox("Style", ["bullet","executive","technical","non_technical"])

            if st.button("Generate Summary", use_container_width=True):
                with st.spinner("Summarizing..."):
                    try:
                        res = requests.get(
                            f"{BACKEND_URL}/summarize_document",
                            params={"style":doc_style, "username": st.session_state.username}
                        )
                        if res.status_code == 200:
                            summary = res.json().get("summary","No summary")
                            st.info(summary)
                        else:
                            st.error("Summarization Failed")
                    except Exception as e:
                        st.error(f"Connection error: {e}")

        elif selection == "🛠️ Tools":
            st.header("Text Summarizer")
            text_input = st.text_area("Input Text", height=150)
            style = st.selectbox("Style", ["bullet","executive","technical","non_technical","custom"], key="text_sum_style")

            custom_instruction = None
            if style == "custom":
                custom_instruction = st.text_input("Custom instruction:")
                
            if st.button("Summarize Text", use_container_width=True):
                with st.spinner("Processing..."):
                    try:
                        res = requests.post(
                            f"{BACKEND_URL}/summarize",
                            json = {
                                "text" : text_input,
                                "style" : style,
                                "custom_instruction" : custom_instruction
                            }
                        )
                        if res.status_code == 200:
                            st.write(res.json()["summary"])
                        else:
                            st.error("Failed")
                    except Exception as e:
                        st.error(f"Error: {e}")
                        
            st.markdown("---")
            st.header("Chat Summary")
            chat_style = st.selectbox("Summary Style", ["bullet","executive","technical","non_technical"], key="chat_sum_style")

            if st.button("Summarize Conversation", use_container_width=True):
                with st.spinner("Analyzing chat..."):
                    try:
                        res = requests.get(
                            f"{BACKEND_URL}/summarize_chat",
                            params={"style":chat_style, "username": st.session_state.username}
                        )
                        if res.status_code ==200:
                            st.write(res.json().get("summary"))
                        else:
                            st.error("Failed")
                    except Exception as e:
                        st.error(f"Error: {e}")

        
        st.markdown("---")
        if st.button("Logout", type="secondary", use_container_width=True):
            st.session_state.username = None
            st.session_state.messages = []
            st.rerun()
            
    return selection
