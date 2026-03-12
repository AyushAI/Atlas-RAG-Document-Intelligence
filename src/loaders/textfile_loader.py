'''
# Load external document using langchain loaders

# 1. Text loader source : https://www.youtube.com/watch?v=bL92ALSZ2Cg

from langchain_community.document_loaders import TextLoader

loader = TextLoader("Day 2/OpenAi.txt", encoding='utf-8')
docs = loader.load()

# it loads the document in the form of a single list

print(docs[0].page_content)

'''

from langchain_core.documents import Document

def load_text_file(file_path):
    with open(file_path, "r", encoding='utf-8') as f:
        text = f.read()
    
    return [Document(page_content=text, metadata = {'source':file_path})]