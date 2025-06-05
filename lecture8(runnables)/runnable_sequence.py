from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence

load_dotenv()

# Define the HuggingFace endpoint
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="Explain the joke: {joke}",
    input_variables=["joke"],
)

parser = StrOutputParser()

chain = RunnableSequence(
    prompt1 | model | parser | prompt2 | model | parser
)

response = chain.invoke({"topic": "AI"})
print(response)  # Output: A joke about AI