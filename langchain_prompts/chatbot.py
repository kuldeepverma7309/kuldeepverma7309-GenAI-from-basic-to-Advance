from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv

load_dotenv()

model_id = "HuggingFaceH4/zephyr-7b-beta"

llm = HuggingFacePipeline.from_model_id(
    model_id=model_id,
    task="text-generation",
    pipeline_kwargs=dict(
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,
    ),
)

model = ChatHuggingFace(llm=llm, model_id=model_id)

while True:
    user_input = input('You: ')
    if user_input.lower() == 'exit':
        print("Exiting the chatbot.")
        break
    response = model.invoke(user_input)
    print(f"Chatbot: {response.content}")