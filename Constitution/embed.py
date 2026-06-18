import json
import sys
import os
import chromadb
from sentence_transformers import SentenceTransformer

ARTICLES_PATH = "articles.json"

CHROMA_DB_PATH = "./chroma_db"

COLLECTION_NAME = "nepal_constitution"

EMBEDDING_MODEL = "intfloat/multilingual-e5-base"

BATCH_SIZE = 32

def load_embedding_model(model_name):
    model = SentenceTransformer(model_name)
    return model

def setup_chromadb(db_path, collection_name):
    client = chromadb.PersistentClient(path=db_path)

    collection = client.get_or_create_collection(
        name = collection_name,
        metadata={"hnsw:space": "cosine"}
    )

    return collection

def embed_and_store(articles, model, collection):
    existing_count = collection.count()