from langchain_community.retrievers import WikipediaRetriever

# Create a WikipediaRetriever instance
wikipedia_retriever = WikipediaRetriever(
    top_k_results=2,
    language="en",
)

# Define your query
query = "BCCI president"

# Get relevant wikipedia documents
docs = wikipedia_retriever.invoke(query)

for doc in docs:
    print(f"Title: {doc.metadata['title']}")
    print(f"Content: {doc.page_content}")  # Print first 500 characters of content