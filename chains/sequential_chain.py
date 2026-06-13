from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model  = ChatOllama(model='qwen3:8b', reasoning= False)
parser = StrOutputParser()

#template 1
template1 = PromptTemplate(
    template="Give a detailed review on the topic {topic}",
    input_variables=['topic']
)


#template2
template2 = PromptTemplate(
    template= "Give main 5 line pointers on the given text \n {text}",
    input_variables=['text']
)


chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic' : "macbooks"})

print(result)
