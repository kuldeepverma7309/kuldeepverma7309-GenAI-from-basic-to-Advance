from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"],
)

# 2nd prompt -> summary

template2 = PromptTemplate(
    template="Write a 5 line summary on the following text. /n {text}",
    input_variables=["text"],
)

prompt1 = template1.format(topic="Artificial Intelligence")
# prompt2 = template2.format(text=prompt1)
response1 = model.invoke(prompt1)

prompt2 = template2.format(text=response1.content)
response2 = model.invoke(prompt2)

print("Detailed Report:")
print(response1.content)
print("\nSummary:")
print(response2.content)