from langchain_ollama import  ChatOllama
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""you have to explain the research paper {paper_input}, with following explanation style {style_input}, with the output size of {length_input}""",
    input_variables= ['paper_input','style_input','length_input'],
    validate_template=True #checks if the variables in template and input is same
)

template.save('template.json')