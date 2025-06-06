# runnable lambda is a runnable primitive that allows you to apply custom python functions within an AI pipeline.
# It acts as a middleware between different AI components, enabling preprocessing, transformation, API calls, filtering and post-processing in a langchain workflow.
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# parallel chain banane ke liye hame runnable ki jarurat hoti hai
from langchain.schema.runnable import RunnableParallel, RunnableSequence, RunnablePassthrough, RunnableLambda

load_dotenv()

# Define the HuggingFace endpoint
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"],
)


parser = StrOutputParser()

joke_gen_chain = RunnableSequence(
    prompt, model, parser
)

def word_count(text: str) -> int:
    """Count the number of words in a text."""
    return len(text.split())

parallel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "word_count": RunnableLambda(word_count)
    }
)

final_chain = RunnableSequence(
    joke_gen_chain,
    parallel_chain,
)

print(final_chain.invoke({"topic": "cats"}))
# Output: {'joke': 'Why did the cat sit on the computer? Because it wanted to keep an eye on the mouse!', 'word_count': 16}