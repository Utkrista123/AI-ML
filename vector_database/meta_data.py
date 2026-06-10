import chromadb

client = chromadb.PersistentClient(
    path = "./chroma_db"
)

collection = client.get_or_create_collection(
    name = "law"
)

documents = [
    "Every citizen has the right to freedom.",
    "No person shall be deprived of life or liberty.",
    "Income tax shall be paid according to law.",
    "A company must register before operating.",
    "Theft is punishable by imprisonment."
]

metadatas = [
    {
        "source": "constitution",
        "article_number": "17",
        "language": "en"
    },
    {
        "source": "constitution",
        "article_number": "16",
        "language": "en"
    },
    {
        "source": "tax_act",
        "article_number": "5",
        "language": "en"
    },
    {
        "source": "company_act",
        "article_number": "12",
        "language": "en"
    },
    {
        "source": "criminal_code",
        "article_number": "101",
        "language": "en"
    }
]

id = []

for i in range (1, len(documents) + 1):
    id.append(str(i))

collection.add(
    documents=documents,
    metadatas=metadatas,
    ids=id
)

result = collection.get()

print(result["metadatas"])