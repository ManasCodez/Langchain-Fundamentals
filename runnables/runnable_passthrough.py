from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


#RunnablePassthorugh simply returns the input as the output thout modifying it 


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
pass_through = RunnablePassthrough()

joke_gen = RunnableSequence(prompt, model, parser)

parallel = RunnableParallel({
    'joke' : RunnableSequence(pass_through),
    'explaination' : RunnableSequence(prompt2, model , parser)
})

chain = RunnableSequence(joke_gen, parallel)

res = chain.invoke({'topic' : 'human'})
print(res)