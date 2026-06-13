from langchain_openai import OpenAI     #OpenAI shows we have imported the llm model
from dotenv import load_dotenv

load_dotenv()


#old methods , dont use this 
llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("how is the new macbook air m5? ")

print(result)
