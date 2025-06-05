from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

repo_id="HuggingFaceH4/zephyr-7b-beta"
llm = HuggingFaceEndpoint(repo_id=repo_id,
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,)


model = ChatHuggingFace(llm=llm)
while True:
    user_input = input('You: ')
    if user_input.lower() == 'exit':
        print("Exiting the chatbot.")
        break
    response = model.invoke(user_input)
    print(f"Chatbot: {response.content}")