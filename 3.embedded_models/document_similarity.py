from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OllamaEmbeddings(model = 'nomic-embed-text',dimensions=300)
documents = [
    "virat kohli is the best indian cricekt player known for agressive play style",
    "narendra modi is the PM of india",
    "MS Dhoni is known as captain cool",
    "jasprit bumrah is the best bowler in the world"
]

query = "who is known as captain cool"

doc_embeds = embedding.embed_documents(documents)
q_embed = embedding.embed_query(query)

scores = (cosine_similarity([q_embed], doc_embeds)[0])
index = np.argmax(scores)
print("index, value of max relevant: ",index,', ', scores[index])

print("relevant data:", documents[index])

