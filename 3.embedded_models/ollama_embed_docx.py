from langchain_ollama import ChatOllama, OllamaEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OllamaEmbeddings(model= 'nomic-embed-text', dimensions=16)

queries = [
    'i am manas',
    'delhi is capital of india',
    'kolkata id capital of west bengal'
]

embeds =embeddings.embed_documents(queries)

print(embeds)