
from langchain_community.document_loaders import Docx2txtLoader

def load_docx(file_path):
    loader = Docx2txtLoader(file_path)
    docs = loader.load()
    
    for doc in docs:
        doc.metadata['source'] = file_path
    
    return docs