from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

parser = StrOutputParser()
model1 = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

model2 = ChatOllama(model="qwen3:8b" ,reasoning=False)

prompt1= PromptTemplate(
    template="Give short and simple notes from the given text\n {text}",
    input_variables=['text']
)

prompt2= PromptTemplate(
    template="Generate a short mcq quiz from the given text \n {text}",
    input_variables=['text']
)


prompt3= PromptTemplate(
    template="""Merge the provided notes and quiz in a single document\n
    notes: {notes} \n quiz: {quiz}""",
    input_variables=['notes',"quiz"]
)


parallel_chain = RunnableParallel({
    "notes" : prompt1| model1| parser,
    "quiz" : prompt2 | model2 | parser
})

merge_chain = prompt3 | model2 | parser

chain = parallel_chain | merge_chain 

text = "Volleyball was invented in 1895 by William G. Morgan. Today, it is played by more than 800 million people worldwide and is one of the most popular sports globally. Each team has 6 players on the court, and the standard net height is 2.43 meters for men and 2.24 meters for women. A team may touch the ball up to three times before sending it over the net, making coordination and teamwork essential for success."


result   = chain.invoke({"text" : text})

print(result)

chain.get_graph().print_ascii()