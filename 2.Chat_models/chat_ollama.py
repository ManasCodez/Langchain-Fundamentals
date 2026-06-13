from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

model = ChatOllama(model = 'qwen3:8b', temperature=0.5)#temperature adds randomness
                                                       #for same input model will almost give the same output if the temperature is zero, if the output differs if the temperature is increased
input =  'what is capital of india'
result=model.invoke(input)

print(result.content)
