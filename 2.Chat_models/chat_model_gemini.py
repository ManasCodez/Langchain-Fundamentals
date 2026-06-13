from langchain_google_genai import ChatGoogleGenerativeAI   # ChatOpenAI means er have imported the chat model
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash',temperature = 0.2,
                                           max_output_tokens = 10)

result = model.invoke("what is capital of india ")
print(result.content)



