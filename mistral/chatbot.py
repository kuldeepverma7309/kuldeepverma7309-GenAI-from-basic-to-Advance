from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

chatModel = ChatOpenAI(
    model="mistralai/mistral-7b-instruct:free",
    openai_api_base="https://openrouter.ai/api/v1",
)

result = chatModel.invoke("What is the capital of India?")
print(result.content)
