from langchain_community.document_loaders.csv_loader import CSVLoader
import pandas as pd

def load_csv(file_path):
    
    df = pd.read_csv(file_path)
    
    loader = CSVLoader(
        file_path=file_path,
        csv_args={
            "delimiter": ",",
            "quotechar": '"',
        },
    )
    
    docs = loader.load()
    
            
    for doc in docs:
        doc.metadata['source'] = file_path
    
    return docs