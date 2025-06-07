from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.retrievers.multi_query import MultiQueryRetriever


# step 1: Define documents
# Relevant health & wellness documents
all_docs = [
    Document(page_content="Regular walking boosts heart health and can reduce symptoms of depression.", metadata={"source": "H1"}),
    Document(page_content="Consuming leafy greens and fruits helps detox the body and improve longevity.", metadata={"source": "H2"}),
    Document(page_content="Deep sleep is crucial for cellular repair and emotional regulation.", metadata={"source": "H3"}),
    Document(page_content="Mindfulness and controlled breathing lower cortisol and improve mental clarity.", metadata={"source": "H4"}),
    Document(page_content="Drinking sufficient water throughout the day helps maintain metabolism and energy.", metadata={"source": "H5"}),
    Document(page_content="The solar energy system in modern homes helps balance electricity demand.", metadata={"source": "I1"}),
    Document(page_content="Python balances readability with power, making it a popular system design language.", metadata={"source": "I2"}),
    Document(page_content="Photosynthesis enables plants to produce energy by converting sunlight.", metadata={"source": "I3"}),
    Document(page_content="The 2022 FIFA World Cup was held in Qatar and drew global energy and excitement.", metadata={"source": "I4"}),
    Document(page_content="Black holes bend spacetime and store immense gravitational energy.", metadata={"source": "I5"}),
]

# step 2: initialize embedding model
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# step 3: create FAISS vector store
vector_store = FAISS.from_documents(
    documents=all_docs,
    embedding=embedding,
)

# step 4: create retrievers
similarity_retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}  # Retrieve top 5 similar documents
)

multiquery_retriever = MultiQueryRetriever.from_llm(
    retriever=vector_store.as_retriever(search_kwargs={"k": 5}),  # Retrieve top 5 documents
    llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct:free",
    openai_api_base="https://openrouter.ai/api/v1"
))

query = "How to improve energy levels and maintain balance?"

# step 5: retrieve documents
similar_docs = similarity_retriever.invoke(query)
multiquery_docs = multiquery_retriever.invoke(query)
# step 6: print results
print("Similarity Retriever Results:")

for i, doc in enumerate(similar_docs):
    print(f"Result {i + 1}. {doc.page_content}")
    print("-" * 80)

print("="*80)
print("Multi-Query Retriever Results:")
for i, doc in enumerate(multiquery_docs):
    print(f"Result {i + 1}. {doc.page_content}")
    print("-" * 80)