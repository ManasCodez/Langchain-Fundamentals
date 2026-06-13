from langchain_ollama import ChatOllama, embeddings
from dotenv import load_dotenv

load_dotenv()

model = ChatOllama(model = 'qwen3:8b', max_output_tokens = 100)
chat_history = []
while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input == 'exit':break

    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print('Chatbot: ', result.content)

print(chat_history)


