from src.processing.splitter import split_documents
from src.processing.vectore_store import create_vector_store
from src.loaders import load_documents

def build_knowledge_base(file_path, db_path="vector_db"):
    
    documents = load_documents(file_path)
    
    chunks = split_documents(documents)
    
    vectorstore = create_vector_store(chunks, db_path)
    
    return vectorstore