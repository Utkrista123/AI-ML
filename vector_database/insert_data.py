import chromadb

client = chromadb.PersistentClient(
    path = "./chroma_db"
)

collection = client.get_collection(
    name = "law"
)

collection.add(
    documents=["Kathmandu is the capital of Nepal"],
    metadatas=[
        {
            "source": "city",
            "article_number": "107",
            "language": "en"
        }
    ],
    ids=["8"]
)

print("saved")