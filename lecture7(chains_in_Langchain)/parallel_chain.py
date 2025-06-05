from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# parallel chain banane ke liye hame runnable ki jarurat hoti hai
from langchain.schema.runnable import RunnableParallel

load_dotenv()

llm1 = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
)

llm2 = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    task="text-generation",
)

model1 = ChatHuggingFace(llm = llm1)
model2 = ChatHuggingFace(llm = llm2)

prompt1 = PromptTemplate(
    template="Generate the short and simple notes from the following text \n {text}",
    input_variables=["text"],
)

prompt2 = PromptTemplate(
    template="Generate 5 short question answer from the follwing text \n {text}",
    input_variables=["text"],
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single document \n Notes: {notes} \n Quiz: {quiz}",
    input_variables=["notes", "quiz"],
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        "notes": prompt1 | model1 | parser,
        "quiz": prompt2 | model2 | parser,
    }
)

merge_chain = prompt3 | model1 | parser

final_chain = parallel_chain | merge_chain

text = "LangChain is a framework for developing applications powered by language models. It provides modular abstractions for working with LLMs, making it easier to build complex applications."

response = final_chain.invoke({"text": text})

print("Notes and Quiz:")
print(response)