from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

model = ChatOllama(model="qwen3:8b")


#prompt 1
template1 = PromptTemplate(
    template="Write a detailed report on the topic {topic}",
    input_variables=['topic']
)


#prompt2
template2 = PromptTemplate(
    template="Write a 5 line summary on the text given below \n {text}",
    input_variables=['text']
)




# Aam jingadi
# prompt1 = template1.invoke({"topic" : "black hole"})
# result = model.invoke(prompt1)

# prompt2 = template2.invoke({"text":result.content})
# result2 = model.invoke(prompt2)

# print(result2.content)





# Mentos jingadi
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model| parser

result = chain.invoke({"topic" : "black holes"})
print(result)
