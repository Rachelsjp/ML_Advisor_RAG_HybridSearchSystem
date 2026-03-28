import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load embedding model (LOCAL, no API cost)
embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Load existing Chroma DB
vectordb = Chroma(
    persist_directory="../chroma_db",
    embedding_function=embedding
)

retriever = vectordb.as_retriever(search_kwargs={"k": 3})


def get_docs_with_scores(query):
    docs = vectordb.similarity_search_with_score(query, k=3)
    return docs