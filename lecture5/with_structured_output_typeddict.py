from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from typing import TypedDict, Annotated, Optional
from dotenv import load_dotenv
import os
load_dotenv()

token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
print(f"token: {token}")
repo_id = "HuggingFaceH4/zephyr-7b-beta"
llm = HuggingFaceEndpoint(repo_id=repo_id,
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,
    huggingfacehub_api_token=token
    )


model = ChatHuggingFace(llm=llm)

class Review(TypedDict):
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list format"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "sentiment of the review, either positive, negative or neutral"]
    pros: Annotated[Optional[list[str]], "List of pros mentioned in the review"]
    cons: Annotated[Optional[list[str]], "List of cons mentioned in the review"]


structured_model = model.with_structured_output(Review)


result = structured_model.invoke("""
I recently purchased the XPhone Pro Max and have been using it for about two weeks now. While the hardware is undeniably impressive — the build quality is excellent, the display is sharp and vivid, and the battery life easily lasts a full day with heavy use — the software experience leaves a lot to be desired.

First off, the phone came with a ton of pre-installed apps, many of which cannot be removed. This not only clutters the app drawer but also takes up a significant amount of internal storage. The user interface feels outdated, with clunky navigation and inconsistent design patterns that are not in line with modern UI trends.

There are also some annoying bugs — for instance, notifications don’t always show up on time, and the fingerprint scanner sometimes takes multiple tries to unlock the device. Additionally, system updates are slow, and it looks like the brand only promises two years of software support, which is disappointing for a flagship phone.

That said, the camera performance is quite good in daylight, though low-light shots are just average. The speakers are loud and clear, and call quality is solid.

Overall, while the phone nails the hardware, the software experience holds it back. I'm hoping the company listens to feedback and pushes out major updates to fix these issues. Right now, it feels like a beautiful car with a clunky engine.
""")


print(f"result: {result}")



