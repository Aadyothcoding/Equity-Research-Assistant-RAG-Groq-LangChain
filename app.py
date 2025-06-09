import streamlit as st
from loader import load_urls_as_docs
from vectorstore import split_and_store
from rag_chain import build_qa_chain

st.set_page_config(page_title="📊 Equity Research Assistant", page_icon="📈")

st.title("📊 Equity Research Assistant (RAG + Groq + LangChain)")
st.markdown("This app helps equity research analysts get answers from financial news articles using LLMs.")

# --- Input Section ---
st.subheader("Step 1: Enter URLs")
url1 = st.text_input("URL 1")
url2 = st.text_input("URL 2")
url3 = st.text_input("URL 3")

st.subheader("Step 2: Enter your question")
question = st.text_input("What would you like to know?")

# --- Action Button ---
if st.button("Search"):
    if not all([url1, url2, url3, question]):
        st.warning("Please fill in all 3 URLs and your question.")
    else:
        with st.spinner("Processing articles and fetching answer..."):
            docs = load_urls_as_docs([url1, url2, url3])
            vectordb = split_and_store(docs)
            qa_chain = build_qa_chain(vectordb)

            # Use invoke instead of run to handle multiple outputs
            response = qa_chain.invoke({"query": question})
            answer = response["result"]
            sources = response["source_documents"]

        st.success("Answer:")
        st.write(answer)

        with st.expander("📚 Source Documents"):
            for i, doc in enumerate(sources, start=1):
                st.markdown(f"**Document {i} Source:** {doc.metadata.get('source', 'N/A')}")
                st.write(doc.page_content[:500] + "...")
