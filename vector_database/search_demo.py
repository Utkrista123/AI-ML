import chromadb

client = chromadb.PersistentClient(
    path= "./chroma_db"
)

collection = client.get_collection(
    name = "facts"
)

results = collection.query(
    query_texts=[
        "Building web applications with Python"
    ],
    n_results=3
)

for doc in results["documents"][0]:
    print(doc)