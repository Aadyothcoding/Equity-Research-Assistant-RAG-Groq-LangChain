# loader.py
from langchain_community.document_loaders import WebBaseLoader

def load_urls_as_docs(urls):
    docs = []
    for url in urls:
        loader = WebBaseLoader(url)
        loaded_docs = loader.load()
        for doc in loaded_docs:
            doc.metadata['source'] = url
        docs.extend(loaded_docs)
    return docs
