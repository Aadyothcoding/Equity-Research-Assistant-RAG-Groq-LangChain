# 📊 Equity Research Agent

An AI-powered assistant for equity analysts that helps analyze company fundamentals, extract insights from financial documents, and retrieve the latest news using LLMs and RAG (Retrieval-Augmented Generation).

---

## 🚀 Features

- 🔍 **Query Financial Documents**: Upload annual reports, earnings calls, or filings and ask questions.
- 🧠 **LLM-Powered Analysis**: Uses Groq API with LLaMA 3 for fast and context-aware responses.
- 🗃️ **Vector Store Indexing**: Documents are embedded with Hugging Face models and stored in ChromaDB for efficient retrieval.
- 📰 **Real-Time News Retrieval**: (Optional) Integrate financial news sources like Yahoo Finance or MarketWatch.
- 📈 **Streamlit Frontend**: Simple, interactive UI to upload documents and ask financial questions.

---

## 🛠️ Tech Stack

| Component        | Tech Used                              |
|------------------|-----------------------------------------|
| LLM Inference     | [Groq API](https://console.groq.com) with LLaMA 3 |
| Embeddings        | Hugging Face `sentence-transformers/all-MiniLM-L6-v2` |
| Vector Store      | [ChromaDB](https://www.trychroma.com/) |
| Document Parsing  | PyMuPDF / PyPDF2                        |
| Frontend UI       | [Streamlit](https://streamlit.io)       |
| Orchestration     | [LangChain](https://www.langchain.com/) with custom agents |
