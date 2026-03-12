'''
# 3. Web base loader

from langchain_community.document_loaders import WebBaseLoader

url = "https://docs.langchain.com/oss/python/langchain/overview"

loader = WebBaseLoader(url)
website = loader.load()


#print(website[0].page_content)
'''

from langchain_community.document_loaders import WebBaseLoader

def load_websites(url):
    loader = WebBaseLoader(url)
    docs = loader.load()
    
    for doc in docs:
        doc.metadata["source"] = url
    
    return docs