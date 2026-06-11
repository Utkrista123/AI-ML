from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer(
    "intfloat/multilingual-e5-base"
)

emb1 = model.encode("constitution")
emb2 = model.encode("संविधान")

score = util.cos_sim(emb1, emb2)

print(score)