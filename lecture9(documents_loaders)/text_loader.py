from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()
# import os
# print(os.getcwd())


llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
)
model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template="Write a summary of the following text: \n{text}",
    input_variables=["text"],
)

parser = StrOutputParser()

chain = prompt | model | parser



model = ChatHuggingFace(llm=llm)


loader = TextLoader("./cricket.txt", encoding="utf-8")

docs = loader.load()

print(docs[0])

print(type(docs))

response = chain.invoke({"text": docs[0].page_content})
print(response)
