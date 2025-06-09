from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

# Create a tool
@tool
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers."""
    return a * b

# tool binding
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct:free",
    openai_api_base="https://openrouter.ai/api/v1",
)

llm_with_tools = llm.bind_tools([multiply])

human_message = HumanMessage('What is 3 times 4?')
messages = [human_message]
ai_message = llm_with_tools.invoke(messages)
messages.append(ai_message)

# print(messages)

tool_message = multiply.invoke(ai_message.tool_calls[0])

messages.append(tool_message)

final_result = llm_with_tools.invoke(messages)
print(f"Final result: {final_result} \n\n Final result.content: {final_result.content}")
