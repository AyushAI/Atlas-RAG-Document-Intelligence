# 🧠 Altas RAG Document Intelligence
### Enterprise-Grade Multi-Document Intelligence System powered by RAG, Gemini LLM, and Semantic Vector Search

OmniDoc-RAG-Engine is an advanced **Retrieval-Augmented Generation (RAG)** application capable of ingesting **multiple document formats** and answering natural language queries based on the provided data.

The system leverages **Google Gemini Flash LLM**, **FAISS vector search**, and **MiniLM sentence embeddings** to build a scalable document intelligence platform.

Built with **Python, Streamlit, and modern AI architecture**, the application enables users to upload documents, perform semantic search, summarize content, and interact with documents conversationally.

---

# ✨ Features

## 📂 Multi-Document Ingestion
Supports a wide variety of document types:

- PDF
- DOC / DOCX
- CSV
- Excel
- TXT
- Images
- PowerPoint
- Web content
- Databases

---

## 🧠 Retrieval-Augmented Generation (RAG)
The system implements a full RAG pipeline:

1. Document Loading
2. Text Chunking
3. Embedding Generation
4. Vector Storage
5. Semantic Retrieval
6. LLM-powered Response Generation

---

## 💬 Conversational AI
Users can interact with documents through a **chat-based interface** powered by **Gemini Flash LLM**.

Features include:

- Context-aware responses
- Chat history tracking
- Multi-turn conversations
- Semantic document retrieval

---

## 📊 Document Summarization
Multiple summarization styles supported:

- Bullet Summary
- Executive Summary
- Detailed Summary
- Key Insights Extraction

---

## 🔐 User Authentication
Secure login system with:

- User credentials
- SQLite database storage
- Session-based authentication

---

## 📁 Vector Database
FAISS is used for:

- Efficient similarity search
- High-speed semantic retrieval
- Scalable vector storage

---

# 🏗️ System Architecture

```
User Query
     │
     ▼
Streamlit UI
     │
     ▼
Query Processing
     │
     ▼
Retriever (FAISS)
     │
     ▼
Relevant Document Chunks
     │
     ▼
Gemini LLM (RAG)
     │
     ▼
Generated Response
```

---

# ⚙️ Tech Stack

| Component | Technology |
|--------|-------------|
| Language | Python 3 |
| Frontend | Streamlit |
| LLM | Gemini 3 Flash Preview |
| Embedding Model | MiniLM L6 v2 Sentence Transformer |
| Vector Database | FAISS |
| Database | SQLite |
| Backend Framework | Python Modular Architecture |
| Logging | CSV Logging System |

---

# 📁 Project Structure

```
.streamlit
 └── config.toml

.env
 ├── bin
 ├── etc
 ├── include
 ├── lib
 └── share

backend
 └── main.py

logging
 └── chat_logs.csv

src
 ├── chatbot
 │    ├── conversation_chain.py
 │    ├── history_manager.py
 │    └── memory.py
 │
 ├── loader
 │    ├── csv_loader.py
 │    ├── db_loader.py
 │    ├── doc_loader.py
 │    ├── docx_loader.py
 │    ├── excel_loader.py
 │    ├── images_loader.py
 │    ├── pdf_loader.py
 │    ├── ppt_loader.py
 │    ├── pptx_loader.py
 │    ├── textfile_loader.py
 │    └── web_loader.py
 │
 ├── logging
 │    └── logger.py
 │
 ├── processing
 │    ├── embedding.py
 │    ├── splitter.py
 │    └── vector_store.py
 │
 ├── rag
 │    ├── gemini_llm.py
 │    ├── prompt_template.py
 │    ├── qa_chain.py
 │    └── retriever.py
 │
 ├── summarizer
 │    ├── summarizer.py
 │    ├── summary_prompt.py
 │    └── summary_styles.py
 │
 └── ui
      ├── chat.py
      ├── login.py
      ├── sidebar.py
      └── styles.py

user_data
 └── user_data

vector_db
 └── vector_database
```

---

# 🔄 RAG Pipeline Workflow

### Step 1 — Document Upload
Users upload documents through the Streamlit interface.

### Step 2 — Document Parsing
Loader modules extract text depending on document type.

### Step 3 — Text Chunking
Large text is split into smaller chunks using the text splitter.

### Step 4 — Embedding Generation
Each chunk is converted into embeddings using:

MiniLM-L6-v2 Sentence Transformer

### Step 5 — Vector Storage
Embeddings are stored inside a FAISS vector index.

### Step 6 — Semantic Retrieval
Relevant document chunks are retrieved based on similarity search.

### Step 7 — LLM Response
Gemini Flash LLM generates responses using retrieved context.

---

# 🚀 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/OmniDoc-RAG-Engine.git
cd OmniDoc-RAG-Engine
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv .env
```

Activate:

**Windows**

```
.env\Scripts\activate
```

**Mac/Linux**

```
source .env/bin/activate
```

---

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 4️⃣ Add Environment Variables

Create `.env` file

```
GEMINI_API_KEY=your_api_key
```

---

## 5️⃣ Run Application

```
streamlit run backend/main.py
```

---

# 🖥️ Application Modules

### Login UI
Handles authentication and user sessions.

### Document Manager
Upload and manage document sources.

### Chat Workspace
Interactive AI conversation interface.

### Vector Database
Stores embeddings for semantic search.

### Summarization Engine
Generates multiple document summaries.

---

# 📊 Logging System

All chat interactions are stored in:

```
logging/chat_logs.csv
```

This enables:

- Conversation tracking
- Debugging
- Analytics

---

# 🔐 Security

- User credential management
- SQLite local database
- Environment variable protection

---

# 📌 Future Improvements

- Multi-user collaboration
- Cloud vector databases (Pinecone / Weaviate)
- Real-time document streaming
- Role-based authentication
- LangGraph agent workflows
- Knowledge graph integration

---

# 🤝 Contribution

Contributions are welcome.

Steps:

1. Fork the repository
2. Create a new feature branch
3. Commit changes
4. Submit pull request

---

# 📜 License

MIT License

---

# 👨‍💻 Author

**Ayush Wase**

AI Engineer | Data Analyst | ML Developer

Specializing in:

- Artificial Intelligence
- Machine Learning
- RAG Systems
- Data Analytics
- NLP Applications

---

⭐ If you like this project, consider giving it a star!
