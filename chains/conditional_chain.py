
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import Field,BaseModel
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

parser = StrOutputParser()

model1= ChatOllama(model = 'qwen3:8b', reasoning= False)

class feedback(BaseModel):
    feed_back : Literal['positive', "negative"] = Field(description="is the review positive or negative")

parser2 = PydanticOutputParser(pydantic_object = feedback)


prompt1= PromptTemplate(
    template="Classify the following review as positive of negative \n {review} \n {format_inst}",
    input_variables= ['review'],
    partial_variables= {'format_inst' : parser2.get_format_instructions()}
)


classifier_chain = prompt1 |model1 | parser2 

prompt2 = PromptTemplate(
    template="Write a appropriate response to this positive feedback \n {review}",
    input_variables=['review']
)

prompt3 = PromptTemplate(
    template="Write a appropriate response to this nogative feedback \n {review}",
    input_variables=['review']
)

branch_chain = RunnableBranch(
    (lambda x: x.feed_back == 'positive', prompt2 | model1 | parser ),
    (lambda x: x.feed_back == 'negative', prompt3 | model1| parser),
    RunnableLambda(lambda x: "could not find the sentiment")
)


chain = classifier_chain | branch_chain 

res = chain.invoke({"review":"this is a wonderful phone"})
print(res)

chain.get_graph().print_ascii()