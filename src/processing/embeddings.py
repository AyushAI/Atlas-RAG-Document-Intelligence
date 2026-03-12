from langchain_community.embeddings import SentenceTransformerEmbeddings

def get_embedding_model():
    return SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")