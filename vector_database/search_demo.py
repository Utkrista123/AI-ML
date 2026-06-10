import chromadb

client = chromadb.PersistentClient(
    path= "./chroma_db"
)

collection = client.get_collection(
    name = "law"
)

results = collection.query(
    query_texts=[
        "what rigts do citizens have?"
    ],
    n_results=3,
    where={
        "source": "city"
    }
)

for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
    print(f"{doc} article_number: {meta ["article_number"]}, language: {meta ["language"]}")
