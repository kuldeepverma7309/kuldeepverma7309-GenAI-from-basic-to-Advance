# runnable branch is a runnable primitive that allows you to create branches in your AI pipeline based on conditions. It enables you to execute different paths in the workflow depending on the input or intermediate results.
# this is used for implementing if else logic in langchain universe.
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# parallel chain banane ke liye hame runnable ki jarurat hoti hai
from langchain.schema.runnable import RunnableParallel, RunnableSequence, RunnablePassthrough, RunnableLambda, RunnableBranch

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
)
model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="Summarize the following text \n {text}",
    input_variables=["text"],
)

parser = StrOutputParser()

report_gen_chain = RunnableSequence(
    prompt1, model, parser
)
# all the if conditions are defined in touples and else defined in default touple
# branch_chain = RunnableBranch(
#     (),
#     (),
#     default=RunnableLambda(lambda x: "No report generated"),
# )

branch_chain = RunnableBranch(
    (lambda x: len(x.split() > 500), RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(
    report_gen_chain,
    branch_chain,
)

print(final_chain.invoke({"topic": "AI in 2050"}))