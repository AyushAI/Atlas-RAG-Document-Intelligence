import os
from langchain_community.vectorstores import FAISS
from src.processing.embeddings import get_embedding_model

DB_PATH = "vector_db"

#vectorization happens here
def create_vector_store(chunks, db_path=DB_PATH):
    embeddings = get_embedding_model() # get your embedding model here
    
    vectorstore = FAISS.from_documents(chunks, embeddings) # embedding model is called for every document chunk
    
    # saving data to local vectorstore
    vectorstore.save_local(db_path)
    print(f"Vector DB created at {db_path}")
    
    
    return vectorstore


def load_vector_store(db_path=DB_PATH):
    embeddings = get_embedding_model()
    
    if not os.path.exists(db_path):
        raise ValueError(f"Vector DB not found at {db_path}.")
    
    return FAISS.load_local(db_path, embeddings, allow_dangerous_deserialization=True)