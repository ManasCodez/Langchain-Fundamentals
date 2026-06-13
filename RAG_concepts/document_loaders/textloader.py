from langchain_community.document_loaders import TextLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()

parser = StrOutputParser()
model = ChatOllama(model='qwen3:8b', reasoning= False)

prompt = PromptTemplate(
    template="Write a short summary on the given text \n {text}",
    input_variables=['text']
)

chain = prompt | model| parser

res = chain.invoke({'text' :docs[0].page_content})
print(res)
