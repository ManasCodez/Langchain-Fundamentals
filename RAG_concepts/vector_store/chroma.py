from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document



docs = [
    Document(
        page_content="Python is a popular programming language used for web development, data science, and artificial intelligence.",

        metadata={"source": "python.txt", "topic": "programming"},
        ),
    Document(
        page_content="The Indian Premier League (IPL) is one of the most watched T20 cricket tournaments in the world.",
        metadata={"source": "sports.txt", "topic": "cricket"},
    ),
    Document(

        page_content="Machine learning enables computers to learn patterns from data and make predictions without being explicitly programmed.",

        metadata={"source": "ml.txt", "topic": "machine_learning"},

    ),

    Document(

        page_content="The Amazon rainforest is the largest tropical rainforest on Earth and is home to an incredible diversity of plants and animals.",

        metadata={"source": "geography.txt", "topic": "nature"},

    ),

    Document(

        page_content="Solar energy is a renewable source of power that converts sunlight into electricity using photovoltaic cells.",

        metadata={"source": "energy.txt", "topic": "renewable_energy"},

    ),

]


vector_store = Chroma(
    embedding_function= OllamaEmbeddings(model='nomic-embed-text'),
    persist_directory='my_chroma_db',
    collection_name='sample'
)

vector_store.add_documents(docs)

res = vector_store.get(include=['embeddings','metadatas','documents'])
print(res)
