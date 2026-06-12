import chromadb
from sentence_transformers import SentenceTransformer
from chromadb.api.types import EmbeddingFunction

model = SentenceTransformer("intfloat/multilingual-e5-base")

class E5EmbeddingFunction(EmbeddingFunction):
    def __init__(self, model):
        self.model = model

    def __call__(self, input):
        inputs = ["passage: " + i for i in input]
        return self.model.encode(inputs, normalize_embeddings=True).tolist()
    def name(self):
        return "E5-encoding"

client = chromadb.PersistentClient("./chroma_multi_db")

collection = client.get_or_create_collection(
    name = "law",
    embedding_function = E5EmbeddingFunction(model)
)

documents = [
    "No person shall be deprived of his or her personal liberty except in accordance with law.",

    "Freedom of opinion and expression.",
    "Freedom to assemble peaceably and without arms.",
    "Freedom to form political parties.",
    "Freedom to form unions and associations.",
    "Freedom to move and reside in any part of Nepal.",
    "Freedom to practise any profession, carry on any occupation and establish and operate any industry, trade and business in any part of Nepal.",

    "Restrictions may be imposed on freedom of opinion and expression to protect sovereignty, territorial integrity, national independence, public morality, contempt of court, defamation, and public decency.",
    "Restrictions may be imposed on freedom to assemble to protect sovereignty, territorial integrity, national security, and public law and order.",
    "Restrictions may be imposed on political party activities related to espionage, national security threats, sedition, caste or communal hatred, violent acts, or discrimination in party formation.",
    "Restrictions may be imposed on unions and associations for national security, public morality, sedition, or harm to inter-community harmony.",
    "Restrictions may be imposed on movement rights for public interest, inter-federal harmony, or prevention of violent acts.",
    "Restrictions may be imposed on profession, trade, and business for public health, morality, national interest, and regulation of industries."
]

metadata = []

for i in range(1, len(documents) + 1):
    dict = {
        "source": "Constiution",
        "article": f"Paragraph: {i}",
        "language": "en"
    }

    metadata.append(dict)

print(metadata)

ids = [str(i) for i in range(1, len(documents) + 1)]

collection.add(
    documents = documents,
    metadatas = metadata,
    ids = ids
)

result_query = collection.query(
    query_texts = "query: के ले मौलिक स्वतन्त्रतालाई प्रतिबन्धित गर्न सक्छ",
    n_results = 1
)

for doc, meta in zip(result_query["documents"][0], result_query["metadatas"][0]):
    print(f"{doc} article_number: {meta ["article"]}, language: {meta ["language"]}")

