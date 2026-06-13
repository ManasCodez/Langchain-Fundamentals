from langchain_ollama import  ChatOllama, OllamaEmbeddings


embeddings = OllamaEmbeddings(model = "nomic-embed-text",dimensions=768) #768 is max for this model

vector= embeddings.embed_query("what is capital of india?")
print(len(vector))
