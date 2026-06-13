from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama

model = ChatOllama(model = 'qwen3:8b',
                   reasoning=False) #model spends less time in thinking
messages = [
    SystemMessage(content=  'You are a helpful assistant'),
]



while True:
    user_input = input("You: ")
    messages.append(HumanMessage(content= user_input))

    if user_input == 'exit': break

    result = model.invoke(messages)
    messages.append(AIMessage(content=result.content))
    print(result.content)

