from huggingface_hub import HfApi

token = "hf_YOUR_TOKEN_HERE"
api = HfApi(token=token)

try:
    info = api.model_info("mistralai/Mixtral-8x7B-Instruct-v0.1")
    print("Model info fetched successfully!")
except Exception as e:
    print("Error fetching model info:", e)
