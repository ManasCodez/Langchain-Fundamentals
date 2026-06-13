from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel
from langchain_core.output_parsers import StrOutputParser


prompt1 = PromptTemplate(
    template="Generate a tweet on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Generate a linkedin post on {topic}",
    input_variables=['topic']
)

model = ChatOllama(model='qwen3:8b', reasoning= False)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2 , model, parser)
})

res = parallel_chain.invoke({'topic': 'AI'})

print(res)
