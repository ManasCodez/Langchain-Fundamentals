# primarily used for text based static sites 
from langchain_community.document_loaders import WebBaseLoader



url = 'https://en.wikipedia.org/wiki/Machine_learning'

loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))
print(docs[0].page_content)
