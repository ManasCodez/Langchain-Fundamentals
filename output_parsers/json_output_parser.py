from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

model = ChatOllama(model="qwen3:8b",
                   reasoning= False)

parser = JsonOutputParser()

template = PromptTemplate(
    template= "Give five fact about {topic} \n {format_inst}",
    input_variables=["topic"],
    partial_variables={"format_inst" : parser.get_format_instructions()}
)


chain = template | model | parser 

final = chain.invoke({"topic" : "black holes"})    #JsonOutputParser can give any structure in the json format

print(type(final))
print(final)
