from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser



loader = PyPDFLoader('Resume.pdf')     #good only for text based pdfs (not images)

docs = loader.load()

parser = StrOutputParser()
model = ChatOllama(model='qwen3:8b', reasoning= False)

print(len(docs))    #len is equal to the number of pages

print(docs[0].page_content)
print(docs[0].metadata)

