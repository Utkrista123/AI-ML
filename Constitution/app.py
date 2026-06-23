import sys
import time
import streamlit as st
from sentence_transformers import SentenceTransformer
import chromadb
import ollama

CHROMA_DB_PATH = "./chroma_db"
COLLECTION_NAME =  "nepal_constitution"
EMBEDDING_MODEL = "intfloat/multilingual-e5-base"
LLM_MODEL = "qwen3:8b"
TOP_K = 5

@st.cache_resource
def load_embedding_model():
    return SentenceTransformer(EMBEDDING_MODEL)

@st.cache_resource
def load_collection():
    client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
    return client.get_collection(name = COLLECTION_NAME)

def check_ollama_ready(model_name):
    try:
        models_response = ollama.list()
        available_models = [m["model"] for m in models_response["models"]]

        model_found = any(
            model_name in m or m.startswith(model_name.split(":")[0])
            for m in available_models
        )

        if not model_found:
            return False, (
                f"Model '{model_name}' not found in Ollama.\n"
            )
        return True, ""
    
    except Exception as e:
        return False, (
            "Could not connect to Ollama. Is it running?\n"
            f"Technical error: {str(e)}"
        )
    
def retrive_articles(query, embed_model, collection, top_k = TOP_K):
    query_embedding = embed_model.encode(
        f"query: {query}",
        normalize_embeddings = True
    )

    results = collection.query(
        query_embedding = [query_embedding.tolist()],
        n_results = top_k,
        include = ["documents", "metadatas", "distances"]
    )

    articles = []
    for doc, meta, distance in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distance"][0]
    ):
        relevance = round((1 - distance / 2) * 100, 1)
        articles.append({
            "article_number": meta["article_number"],
            "text": doc,
            "relevance": relevance
        })
    return articles