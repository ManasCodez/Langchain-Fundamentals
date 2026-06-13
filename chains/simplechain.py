from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate(
    template= "generate 5 interesting facts about {topic}",
    input_variables=['topic']
)


model = ChatOllama(model = 'qwen3:8b', reasoning= False)

parser = StrOutputParser()

chain = prompt | model | parser     # |  is also called pipe operator


result = chain.invoke({"topic" : "volleyball"})
print(result)
chain.get_graph().print_ascii()

