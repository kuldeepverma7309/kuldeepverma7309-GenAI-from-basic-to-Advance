## What are Retrievers?
A retriever is a component in LangChain that fetches relevant documents from a data source in response to a user's query.

There are multiple types of retrievers. All retrievers in LangChain are runnables.its mean we can form chain using retrievers.

## Types of Retrievers Based on Data Source
1. wikipedia retriever
2. vector store retriever
3. Archive retriever

## Types of Retrievers based on search strategy
1. MMR (Maximal Marginal Relevance) Retriever
2. Multi Query Retriever
3. contextual compression retriever

***There are more than 20 retrievers available in LangChain.***

## Wikipedia Retriever
A wikipedia retriever is a retriever that queries the wikipedia API to fetch relevant content for a given query.

***How it works:***
1. It takes a query as input.. you give it a query (e.g., "What is LangChain?").
2. It sends a query to the Wikipedia API.
3. it retrieves the most relevant articles.
4. it return them as Langchain documents.

## Vector Store Retriever
A vector store retriever in LangChain is the most common type of retriever that lets you search and fetch documents from a verctor store based on semantic similarity using vector embeddings.

***How it works:***
1. You store your documents in a vector store (like FAISS, Chroma, or Pinecone).
2. Each document is converted into a dense vector using an embedding model.
3. When the user enters a query:
    - It's also turned into a vector.
    - The retriever compares the query vector with the stored vectors.
    - It retrieves the top-k most similar ones.

## Maximal Marginal Relevance (MMR) Retriever
***How can we pick results that are not relevant to the query but also different from each other?***
MMR is an information retrieval algorithm designed to reduce redundancy in the retrieved results while maintaining high relevance to the query.

## Why MMR Retrievar?
in regular similarity search, you may et documents that are:
- All very similar to each other
- Repeating the same info
- Lacking diverse perspectives

***MMR Retriever avoids that by***
- Picking the most relevant document first.
- Then, picking the next most relevant and least similar to already picked documents.
- And so on...

This helps especially in RAG pipelines where:
- You want your context window to contain diverse but still relevant information.
- Especially useful when documents are semantically overlapping.


## Multi Query Retriever
Sometimes a single query might not capture all the ways information is phrased in your documents.
For Example:
***Query: "How can i stay healthy?"***
Could mean:
- What should i eat?
- How often should i exercise?
- How can i manage stress?

A simple similarity search might miss documents that talk about those things but don't use the word "healthy".

A Multi Query Retriever tries to handle the ambiguity of Queries by generating multiple queries from the original one. such as:
- "What are the best foods to maintain good health?"
- "How can I improve my fitness?"
- "What are some effective stress management techniques?"
- "how can i improve my immune system?"
- "What are the benefits of regular exercise?"
- "How can I maintain a balanced diet?"

***ye query ka different version generate krne ke liye llm ka use krta hai.***


## Contextual Compression Retriever
The Contextual Compression Retriever in LangChain is an advanced retriever that improves retrieval quality by compressing documents after retrieval - keeping only the relevant content based on the user's query.

***Query: "What is photosynthesis?"***

***Retrieved documents by a traditional retriever:***
- "The Grand cany on is a famous natural site. photosynthesis is how plants convert light into energy. many tourists visit every year."

## Problem:
- The retriever returns the entire paragraph
- Only one sentence is actually relevant to the query
- The rest is irrelevant noise that waste context window and may confuse the llm.

## Solution: What contextual Compression Retriever does?
Returns only the relevant part e.g.
"photosynthesis is how plants convert light into energy."

***How it works:**
1. Base Retriever (e.g. FAISS, Chroma) retrieves N documents.
2. A compressor (usually an LLM) is applied to each document.
3. The compressor keeps only the parts relevant to the query.
4. Irrelevant parts are removed.

***When to use it?***
- Your documents are long and contain mixed information.
- You want to reduce context length for LLMs.
- You need to improve answer accuracy in RAG pipelines.