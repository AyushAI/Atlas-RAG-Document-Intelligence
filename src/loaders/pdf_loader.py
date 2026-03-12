def load_pdf(file_path):
    '''this function takes pdf as input'''
    from langchain_community.document_loaders import PyPDFLoader 
    loader = PyPDFLoader(file_path)
    docs = loader.load()
            
    for doc in docs:
        doc.metadata['source'] = file_path
    
    return docs