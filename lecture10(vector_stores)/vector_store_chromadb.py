from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.schema import Document

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
doc1 = Document(
    page_content="Virat Kohali is a famous Indian cricketer. He is known for his aggressive batting style and has been the captain of the Indian national team. He has numerous records in international cricket, including being one of the fastest to score 8000 runs in ODIs.He is captain of the RCB team in the IPL.",
    metadata={"team":"RCB"},
    id=1
)

doc2 = Document(
    page_content="Rohit Sharma is another famous Indian cricketer. He is the captain of the MI team in the IPL. He is known for his elegant batting style and has scored multiple double centuries in ODIs.",
    metadata={"team":"MI"},
    id=2
)

doc3 = Document(
    page_content="MS Dhoni is a legendary Indian cricketer. He is known for his calm demeanor and exceptional leadership skills. He has led India to numerous victories, including the 2007 T20 World Cup and the 2011 ODI World Cup. He is also the captain of the CSK in the IPL.",
    metadata={"team":"CSK"},
    id=3
)

docs = [doc1, doc2, doc3]
# ============================ Create a vector store ============================================
# Initialize the Chroma vector store with the embedding function
vector_store = Chroma(
    embedding_function=embedding,
    collection_name="cricketers",
    persist_directory="chroma_db"
)
# ============================ Add documents to the vector store ============================================
# vector_store.add_documents(docs)
# print("Documents added to the vector store.")

# View documents

# print(vector_store.get(include=['embeddings', 'metadatas', 'documents']))

# ============================ Search for a document ============================================
query = "Who is the captain of the MI team?"
results = vector_store.similarity_search(query, k=1)
# print(f"Search results for query '{query}':\n {results}\n")

# ============================ search with similarity score ============================================
results_with_scores = vector_store.similarity_search_with_score(query, k=1)
print(f"Search results with scores for query '{query}':\n {results_with_scores}\n")


# ============================ Metadata filtering ============================================
result_with_metadata = vector_store.similarity_search_with_metadata(
    query="",
    filter={"team": "CSK"},
)
print(f"Search results with metadata filtering:\n {result_with_metadata}\n")

# ============================ Update document ============================================
# Update the content of the document with id 1
updated_doc1 = Document(
    page_content="Virat Kohli is a famous Indian cricketer. He recently own IPL trophy with RCB team.",
    metadata={"team": "RCB"},
    id=1
)
vector_store.update_document(document_id=1, document=updated_doc1)

# ============================= Delete Document ============================================
# Delete the document with id 2
vector_store.delete(ids=[2])