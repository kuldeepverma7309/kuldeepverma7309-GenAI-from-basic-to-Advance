## What are vector stores
A vector store is a system designed to store and retrieve data represented as numerical vectors.

## Key Features
**1. Storage** - Ensure the vectors and their associated metadata are retained, ehether in-memory for quick lookups or on-disk for durability and large-scale use.

**2. Similarity Search** - Helps retrieve the vectors most similar to a query vector.

**3. indexing** - Provide a data structure or method that enables fast similarity searches on high-demensional vectors(e.g., approzimate nearest neighbors lookups).

**4. CRUD Operations** - Manage the life cycle of data adding new vectors, reading them, updating existing entries, removing outdated vectors.

## Use cases - 
1. semantic search
2. RAG
3. Recommender Systems
4. Image/Multimedia search

## Vector Store Vs Vector Database
**Vector Store** - It generally provide a simpler interface for storing and retrieving vectors, often focusing on similarity search. Ex - FAISS

**Vector Database** - when the database features such as distributed storage, backup and recovery, transaction, concurrency control, authentication and authorization added to the vector store, it becomes a vector database. EX - Milvus, Qdrant, Weaviate, Pinecone

**Vector database is effectively a vector store with additional database capabilities.**

## Vector stores in LangChain
**Supported Vector Stores** - LangChain integrate with multiple vector stores (e.g., FAISS, Milvus, Qdrant, Pinecone, Weaviate) to provide a unified interface for vector operations.

**Common Interfaces** - LangChain provides a common interface for vector stores, allowing developers to switch between different vector stores without changing their code significantly.

**Metadata Handling** - Most vector stores in LnagChain allow you to attach metadata (e.g., timestamps, authors) to each document, enabling filter-based retrieval.

## Chroma Vector Store
Chroma is a lightweight, open-source vector database that is especially friendly for local development and small to medium scale production needs.