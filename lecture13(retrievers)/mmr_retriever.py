from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.schema import Document

# step 1: Define documents

docs = [
    Document(page_content="LangChain makes it easy to work with LLMs"),
    Document(page_content="LangChain is used to build LLMs based applications"),
    Document(page_content="Chroma is used to store and search document embeddings"),
    Document(page_content="Embeddings are vector representations of text"),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone and many more.")
]

# step 2: initialize embedding model

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# step 3: create FAISS vector store from documents
vector_store = FAISS.from_documents(
    documents=docs,
    embedding=embedding,
)
# step 4: convert vector store to retriever and enable MMR
retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 3,  # Retrieve top 3 similar documents
        "lambda_mult": 0.5,  # MMR diversity parameter. if we set it to 0 then then we get most diverse results. if we set it to 1 then it will behave as similarity search.
    }
)

query = "What is LangChain?"
# step 5: retrieve relevant documents
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"Result {i + 1}:")
    print(f"Content: {doc.page_content}")
    print("-" * 80)
