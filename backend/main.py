from fastapi import FastAPI, UploadFile, File, Query, Body, Form, HTTPException
from pydantic import BaseModel
import os
import shutil
import sqlite3
import json

from src.loaders import load_documents
from src.processing import build_knowledge_base
from src.chatbot.memory import ConversationMemory
from src.chatbot.conversation_chain import chat_with_memory
from src.summarizer.summarizer import summarize_document

app = FastAPI()

# Database Setup
DB_FILE = "users.db"
USER_DATA_DIR = "user_data"
VECTOR_DB_DIR = "vector_db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()
    conn.close()

init_db()

# Global dictionary to store active sessions (in-memory cache)
# {username: {"memory": ConversationMemory}}

sessions = {}

# Schemas
class User(BaseModel):
    username: str
    password: str

class QuestionRequest(BaseModel):
    question : str
    username: str
    model: str = "models/gemini-3-flash-preview"

    
class SummaryRequest(BaseModel):
    text : str
    style : str = "bullet"
    custom_instruction : str | None=None

# Auth Endpoints

@app.post("/register")
def register(user: User):
    try:
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("INSERT INTO users VALUES (?, ?)", (user.username, user.password))
        conn.commit()
        return {"message": "User registered successfully"}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Username already exists")
    finally:
        conn.close()

@app.post("/login")
def login(user: User):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (user.username, user.password))
    result = c.fetchone()
    conn.close()
    
    if result:
        # Load history if exists
        session = load_user_session(user.username)
        # Convert history to frontend format
        frontend_history = []
        for turn in session["memory"].get_history():
            frontend_history.append({"role": "user", "content": turn["user"]})
            frontend_history.append({"role": "assistant", "content": turn["bot"]})
            
        return {
            "message": "Login successful", 
            "username": user.username,
            "history": frontend_history
        }
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

def load_user_session(username):
    if username not in sessions:
        memory = ConversationMemory()
        history_path = os.path.join(USER_DATA_DIR, username, "history.json")
        memory.load_from_json(history_path)
        sessions[username] = {"memory": memory}
    return sessions[username]


def save_user_session(username):
    if username in sessions:
        memory = sessions[username]["memory"]
        history_path = os.path.join(USER_DATA_DIR, username, "history.json")
        memory.save_to_json(history_path)

# upload document and build rag

@app.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    username: str = Form(...)
):
    # Ensure user session is loaded
    load_user_session(username)
    
    user_dir = os.path.join(USER_DATA_DIR, username)
    os.makedirs(user_dir, exist_ok=True)
    
    save_path = os.path.join(user_dir, f"temp_{file.filename}")
    db_path = os.path.join(VECTOR_DB_DIR, username)
    
    # Save uploaded file
    with open(save_path,"wb") as buffer:
        buffer.write(await file.read())
        
    # load raw document text
    documents = load_documents(save_path)
    document_text = "\n".join(doc.page_content for doc in documents)
    
    # build vector DB for this user (persistent path)
    build_knowledge_base(save_path, db_path)
    
    # Store doc text in session (optional, for summary)
    sessions[username]["doc_text"] = document_text
    
    # Cleanup temp file
    if os.path.exists(save_path):
        os.remove(save_path)
    
    return {"messages": "Knowledge base updated successfully for user"}

import time
from src.logging.logger import logger

# chat endpoint [rag]
@app.post("/chat")
def chat(request : QuestionRequest):
    username = request.username
    start_time = time.time()
    
    # Ensure session loaded
    session = load_user_session(username)
    memory = session["memory"]
    db_path = os.path.join(VECTOR_DB_DIR, username)
    
    # Check if vector db exists
    if not os.path.exists(db_path):
         return {"answer": "No documents found. Please upload a document to start chatting."}

    response, _, usage = chat_with_memory(request.question, memory, db_path, model=request.model)
    
    # Save history after turn
    save_user_session(username)
    
    end_time = time.time()
    latency_ms = (end_time - start_time) * 1000
    
    # Log interaction
    logger.log_interaction(
        username=username,
        query=request.question,
        response=response,
        latency_ms=latency_ms,
        prompt_tokens=usage.get("prompt_tokens", 0),
        completion_tokens=usage.get("completion_tokens", 0),
        total_tokens=usage.get("total_tokens", 0)
    )
    
    return {"answer": response}

# summarizer endpoint (generic text)
@app.post("/summarize")
def summarize(request: SummaryRequest):
    summary, usage = summarize_document(
        text=request.text,
        style = request.style,
        custom_instructions=request.custom_instruction
    )
    
    return {"summary": summary, "usage": usage}


#  conversation summarizers

@app.get("/summarize_chat")
def summarize_chat(style: str = Query("bullet"), username: str = Query(...)):
    session = load_user_session(username)
    memory = session["memory"]
    conversation_text = memory.get_conversation_text()
    
    if not conversation_text.strip():
        return {"summary":"No conversation available to summarize"}
    
    summary, usage = summarize_document(
        text = conversation_text,
        style= style
    )
    
    return {"summary": summary, "usage": usage}


# summarize uploaded document

@app.get("/summarize_document")
def summarize_uploaded_document(style:str = "bullet", username: str = Query(...)):
    session = load_user_session(username)
    doc_text = session.get("doc_text", "")
    
    if not doc_text:
        return {"summary":"No document uploaded in this active session. (Note: Only current session uploads are summarizable for now)"}
    
    summary, usage = summarize_document(
        text=doc_text,
        style=style 
    )
    
    return {"summary": summary, "usage": usage}