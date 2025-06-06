from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# parallel chain banane ke liye hame runnable ki jarurat hoti hai
from langchain.schema.runnable import RunnableParallel, RunnableSequence

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
    template="Generate a tweet about {topic}",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="Generate linkedin post about {topic}",
    input_variables=["topic"],
)


parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        "tweet": RunnableSequence(prompt1, model1, parser),
        "linkedin": RunnableSequence(prompt2, model2, parser),
    }
)

response = parallel_chain.invoke({"topic": "AI"})
print(response)  # Output: {'tweet': 'A tweet about AI', 'linkedin': 'A LinkedIn post about AI'}
