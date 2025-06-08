## What is the need of RAG?
LLMs can not provide information about: 1. Private data, 2. Recent data, 3. Halucination (false information with confidence).
But the above problems can be solved by fine-tuning. there are three types of fine-tuning: 1. Supervised fine-tuning, 2. Reinforcement learning from human feedback (RLHF) 3. Continued pre-training (CPT). But fine-tuning is costly and time-consuming.

## What is RAG?
RAG is a way to make a language model smarter by giving it extra information at the time you ask your question. In this process user's query and context both are passed to the LLM. LLM will generate the answer based on the context provided and its own parametric knowledge. RAG is a combination of two steps: 1. Information Retrieval, 2. Text Generation.

## Example: """You are a helpful assistant. Answer the question ONLY from the provided context. If the answer is not in the context, say "I don't know". Context: {context} Question: {query} Answer:"""

## How RAG works?
There are 4 steps to build a RAG system:
1. ***Indexing -*** This step involves creating an External Knowledge Base from the documents. This EKB is used to drieve the context that we pass along with the query to the LLM.
2. ***Retrieval -*** This step involves retrieving the relevant context from the EKB based on the user's query.
3. ***Augmentation -*** This step involves creating prompt by combining the user's query with the retrieved context. This add extra knowledge to the llms parametric knowledge.
4. ***Generation -*** This step involves passing the augmented prompt to the LLM to generate the answer.

in shorts, ***Query + Context = Augmented Prompt -> LLM -> Answer***
 
