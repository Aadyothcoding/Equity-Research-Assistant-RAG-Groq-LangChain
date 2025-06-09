# rag_chain.py
from langchain.chains import RetrievalQA
from groq_config import get_groq_llm

def build_qa_chain(vectordb):
    llm = get_groq_llm()
    retriever = vectordb.as_retriever()
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True  # So we get both answer and sources
    )
    return chain
