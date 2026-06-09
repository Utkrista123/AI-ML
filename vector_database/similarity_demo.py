from sentence_transformers import SentenceTransformer
from sentence_transformers import util

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

sentences = [
    "A thief stole property",
    "Theft of goods occurred",
    "The weather is nice",
    "A robbery happened yesterday",
    "It is sunny today",
    "Someone stole my bicycle"
]

embeddings = model.encode(sentences)

highest_score = 0
sen1 = ""
sen2 = ""

for i in range(len(sentences)):
    for j in range(i+1, len(sentences)):
        score = util.cos_sim(
            embeddings[i],
            embeddings[j]
        ).item()

        if highest_score < score:
            highest_score = score
            sen1 = sentences[i]
            sen2 = sentences[j]

        print(sentences[i] + "<->" + sentences[j])
        print(f"Similarity: {score:.4f}")
        print("-" * 40)
    
print("The highest score is: ")
print(f"{sen1 } <--->  {sen2}  :  {highest_score:.4f}")

