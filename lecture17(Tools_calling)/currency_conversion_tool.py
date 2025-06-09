from langchain_openai import ChatOpenAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.tools import tool, InjectedToolArg
from langchain_core.messages import HumanMessage
import requests
from typing import Annotated
from dotenv import load_dotenv
import os

load_dotenv()
EXCHANGE_RATE_API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")
# There will be two tools: one for currency conversion factor and another for multiplication with the factor

@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """This function fetches the currency conversion factor between the base and target currencies."""
    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}/pair/{base_currency}/{target_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)
        data = response.json()
        return data["conversion_rate"]  # Assumes the API response contains this field
    except Exception as e:
        print(f"Error fetching conversion factor: {e}")
        return None
    
# conversion_factor = get_conversion_factor.invoke({"base_currency": "USD", "target_currency": "INR"})
# print(f"Conversion factor from USD to INR: {conversion_factor}")

@tool
def convert_currency(base_currency_value: float, conversion_factor: Annotated[float, InjectedToolArg]) -> float:
    """This function converts the base currency value to the target currency by multiplying the conversion factor."""
    return base_currency_value * conversion_factor

# converted_value = convert_currency.invoke({"base_currency_value": 100, "conversion_factor": 90})
# print(f"Converted value: {converted_value}")

# tool binding
# llm = ChatOpenAI(
#     model="mistralai/mistral-7b-instruct:free",
#     openai_api_base="https://openrouter.ai/api/v1",
# )

hugging_face_endpoint = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="text-generation",
)
llm = ChatHuggingFace(llm=hugging_face_endpoint)

llm_with_tools = llm.bind_tools([get_conversion_factor, convert_currency])

messages = [
    HumanMessage("What is the conversion rate from USD to INR? I have 100 USD and want to convert it to INR. How much will I get?"),
]

ai_message = llm_with_tools.invoke(messages)
messages.append(ai_message)
print(f"AI response: {ai_message.tool_calls}")


for tool_call in ai_message.tool_calls:
    # Execute the 1st tool call and get the conversion factor
    # then i have to pass the conversion factor to the 2nd tool call
    if tool_call["name"] == "get_conversion_factor":
        tool_message1 = get_conversion_factor.invoke(tool_call)
        print(f"Conversion factor: {tool_message1}")
        conversion_rate = tool_message1.content
        messages.append(tool_message1)
    if tool_call["name"] == "convert_currency":
        # fetch the current argument
        tool_call["args"]["conversion_factor"] = conversion_rate
        tool_message2 = convert_currency.invoke(tool_call)
        print(f"Converted value: {tool_message2}")
        messages.append(tool_message2)

final_result = llm_with_tools.invoke(messages)
print(f"Final result: {final_result} \n\n Final result.content: {final_result.content}")
