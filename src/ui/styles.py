import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        /* General App Styling */
        .stApp {
            background-color: #0e1117;
        }
        
        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #262730;
            border-right: 1px solid #333;
        }
        
        /* Chat Message Styling */
        .stChatMessage {
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 10px;
        }
        
        [data-testid="stChatMessageAvatarUser"] {
            background-color: #4a90e2;
        }
        
        [data-testid="stChatMessageAvatarAssistant"] {
            background-color: #50e3c2;
        }
        
        /* Headers */
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Inter', sans-serif;
            color: #fafafa !important;
        }
        
        /* Buttons */
        .stButton button {
            background-color: #4a90e2;
            color: white;
            border-radius: 8px;
            border: none;
            padding: 10px 20px;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .stButton button:hover {
            background-color: #357abd;
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }
        
        /* Inputs */
        .stTextInput input, .stTextArea textarea {
            background-color: #1e1e1e;
            color: #fafafa;
            border-radius: 8px;
            border: 1px solid #444;
            padding: 10px;
        }
        
        .stTextInput input:focus, .stTextArea textarea:focus {
            border-color: #4a90e2;
        }
        
        /* Tab Styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 20px;
        }
        
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            white-space: pre-wrap;
            background-color: transparent;
            border-radius: 4px 4px 0 0;
            color: #aaa;
            font-weight: 600;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: transparent;
            border-bottom: 3px solid #4a90e2;
            color: #4a90e2;
        }
        
        /* Radio Button (Navigation) */
        .stRadio label {
            color: #fafafa;
            font-size: 16px;
            padding: 10px;
            border-radius: 5px;
            transition: background 0.3s;
        }
        
        .stRadio label:hover {
            background-color: #333;
        }
        
        </style>
    """, unsafe_allow_html=True)
