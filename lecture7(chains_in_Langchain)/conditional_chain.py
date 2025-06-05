from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
# parallel chain banane ke liye hame runnable ki jarurat hoti hai
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

class FeedbackResponse(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="The sentiment of the feedback, either positive or negative."
    )

parser2 = PydanticOutputParser(pydantic_object=FeedbackResponse)

prompt1 = PromptTemplate(
    template="Classify the following text into positive or negative sentiment \n {feedback} \n {fromat_instructions}",
    input_variables=["feedback"],
    partial_variables={
        "fromat_instructions": parser2.get_format_instructions(),
    },
)

classifier_chain = prompt1 | model | parser2

# result = classifier_chain.invoke(
#     {
#         "feedback": "I love the new features in this product! It's amazing and has made my life so much easier.",
#     }
# )

# print("Sentiment Classification Result:")
# print(result.sentiment)

prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=["feedback"],
)

prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback \n {feedback}",
    input_variables=["feedback"],
)


branch_chain = RunnableBranch(
   (lambda x: x.sentiment == "positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "negative", prompt3 | model | parser),
    RunnableBranch(lambda x: "could not find sentiment")
)

final_chain = classifier_chain | branch_chain
feedback = "I love the new features in this product! It's amazing and has made my life so much easier."
response = final_chain.invoke({"feedback": feedback})
print("Feedback Response:") 
print(response)