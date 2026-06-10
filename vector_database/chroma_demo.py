import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name = "facts"
)

documents = [
    "Kathmandu is the capital of Nepal.",
    "Mount Everest is the highest mountain.",
    "Python is a programming language.",
    "A thief stole property from a house.",
    "The weather is sunny today.",
    "Water boils at 100 degrees Celsius.",
    "The Earth revolves around the Sun.",
    "A robbery occurred at the bank.",
    "Streamlit is used for web apps.",
    "Dogs are loyal animals."
]

ids = []
for i in range(1, len(documents) + 1):
    ids.append(str(i))

collection.add(
    documents = documents,
    ids = ids
)

print(collection.count())