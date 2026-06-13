from langchain_ollama import ChatOllama

from langchain_core.prompts import ChatPromptTemplate


chat_template = ChatPromptTemplate([
    ('system',"You are a helpful {domain} expert" ),
    ('human',"Explain in simple terms, what is {topic}")

])

model = ChatOllama(model='qwen3:8b', temperature=0)
prompt = chat_template.invoke({'domain':'cricket', 'topic': ' LBW'})
result = model.invoke(prompt)

print(result.content)

