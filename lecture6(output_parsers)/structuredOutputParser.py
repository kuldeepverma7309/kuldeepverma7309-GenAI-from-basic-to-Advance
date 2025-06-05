# structured output parser me ham schema ko enforce kr sakte hain. balki strOutparser aur jsonOutputParser me bhi schema enforce hota hai, lekin structuredOutputParser me hum schema ko define karte hain aur usi ke according output milta hai.

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

# Define the response schema
response_schemas = [
    ResponseSchema(name="fact_1", description="Fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="Fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="Fact 3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(response_schemas)

template = PromptTemplate(
    template="Give me three facts about {topic} \n {format_instructions}",
    input_variables=["topic"],
    partial_variables={
        'format_instructions': parser.get_format_instructions()
    }
)

# prompt = template.invoke({"topic": "Artificial Intelligence"})
# response = model.invoke(prompt)
# result = parser.parse(response.content)
# print("Response: ", response)
# print("Parsed Result: ", result)

chain = template | model | parser
response = chain.invoke({"topic": "Artificial Intelligence"})
print("Response: ", response)