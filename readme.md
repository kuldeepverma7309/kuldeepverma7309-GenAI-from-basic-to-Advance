## model 1
repo_id="deepseek-ai/DeepSeek-R1"
llm = HuggingFaceEndpoint(repo_id=repo_id,
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,)


## model 2
repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1"
llm = HuggingFaceEndpoint(repo_id=repo_id,
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,)

## model 3

repo_id="HuggingFaceH4/zephyr-7b-beta"
llm = HuggingFaceEndpoint(repo_id=repo_id,
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,)
