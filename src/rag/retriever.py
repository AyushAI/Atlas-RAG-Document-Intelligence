from src.processing.vectore_store import load_vector_store

def get_retriever(db_path="vector_db"):
    
    vectorstore = load_vector_store(db_path)
    
    retriever = vectorstore.as_retriever( search_type="similarity", search_kwargs={'k':4})
    
    return retriever