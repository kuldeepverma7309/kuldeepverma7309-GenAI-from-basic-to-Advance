from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a detailed report on {topic}",
        input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="Generate a 5 point summary of the following text \n {text}",
    input_variables=["text"],
)

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

chain = prompt1 | model | prompt2 | model | parser

response = chain.invoke({"topic": "Artificial Intelligence"})

print(response)

# to visualize the chain

chain.get_graph().print_ascii()