from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser


model = ChatOllama(model='qwen3:8b', reasoning=False)


def word_counter(text):
    return len(text.split())



prompt1 = PromptTemplate(
    template="Write a joke on the topic {topic}",
    input_variables=['topic']
)


parser = StrOutputParser()

joke_gen = RunnableSequence(prompt1 , model , parser)

parallel = RunnableParallel({
    'joke' :RunnablePassthrough(),
    'Word_count' : RunnableLambda(word_counter)
})

chain = joke_gen | parallel

res = chain.invoke({'topic':'Cricket'})
print(res)