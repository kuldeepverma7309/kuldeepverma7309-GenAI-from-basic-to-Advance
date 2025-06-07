from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.schema import Document


# step 1: Define documents
documents = [
    Document(page_content="Langchain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors for similarity search."),
    Document(page_content="HuggingFace provides powerful models for text embeddings."),
]

# step 2: initialize embedding model

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# step 3: create chroma vector store in memory

vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embedding,
    collection_name="example_collection",
    # persist_directory="chroma_db",  # Optional: specify a directory to persist the vector store
)

# step 4: convert vector store to retriever
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 2}  # Retrieve top 2 similar documents
)

query = "what is chroma used for?"
# step 5: retrieve relevant documents
results = retriever.invoke(query)
for doc in results:
    print(f"Content: {doc.page_content}")
    print("-" * 40)

