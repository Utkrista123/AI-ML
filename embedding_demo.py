from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

sentence = "Hello world"
embedding = model.encode(sentence)

print(len(embedding))