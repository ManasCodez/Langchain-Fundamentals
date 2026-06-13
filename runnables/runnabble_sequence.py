from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate(
    template="Write a joke on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Explain the given joke \n {joke}",
    input_variables=['joke']
)

model = ChatOllama(model='qwen3:8b', reasoning=False)

parser = StrOutputParser()

chain = RunnableSequence(prompt, model, parser, prompt2, model, parser)

res = chain.invoke({'topic' : 'government'})
print(res)
