from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, PydanticOutputParser
from pydantic import Field, BaseModel


model = ChatOllama(model="qwen3:8b",
                   reasoning= False)

class Person(BaseModel):
    name :str = Field(description="Name of the person")
    age :int = Field(gt=18, description="age of the person" )
    city: str = Field(description="City where the person lives")



parser = PydanticOutputParser(pydantic_object=Person)


template = PromptTemplate(
    template="give name, age and city of a {place}fictional person \n {format_inst}",
    input_variables=['place'],
    partial_variables={"format_inst" : parser.get_format_instructions()}
)


prompt = template.invoke({"place":"Indian"})

chain = template | model | parser

result  = chain.invoke({"place":"Indian"})

print(type(result))
print(result)







