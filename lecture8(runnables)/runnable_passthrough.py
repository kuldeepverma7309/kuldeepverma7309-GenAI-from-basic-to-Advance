# runnable passthrough is a special runnalble premitive that simply returns the input as output without modifying it.

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# parallel chain banane ke liye hame runnable ki jarurat hoti hai
from langchain.schema.runnable import RunnableParallel, RunnableSequence

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
)

