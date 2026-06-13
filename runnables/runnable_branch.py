from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model='qwen3:8b', reasoning=False)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Summarise the following text \n {text}",
    input_variables=['text']
)

report = prompt1 | model | parser

branch = RunnableBranch(
    (lambda x: len(x.split()) > 300 , prompt2 | model | parser),
    RunnablePassthrough()
)

chain = report | branch

res = chain.invoke({'topic':'AI'})

print(res)
