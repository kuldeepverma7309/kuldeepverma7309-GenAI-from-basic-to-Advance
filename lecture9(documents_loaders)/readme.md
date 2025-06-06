## RAG -
RAG is a technique that combines informmation retrieval with language generation, where a model retrieves relevant documents from a knowledge based and then uses them as context to generate accurate and grounded responses.

Benifits of using RAG
1. use of up to date information
2. better privacy
3. No limit of document size

## Components - 
1. Document Loaders
2. Text Splitters
3. Vector Databases
4. Retrivers

## Document Loaders - 
Document loaders are components in langchain used to load data from various sources into a standardized format (usually as a document objects), which can then be used for chunking, embedding, retrieval and generation.

ex - 

Document (
    page_content="The actual text content",
    metadata={"source":"filename.pdf",...}
)

## TextLoader -
TextLoader is a simple and commonly used document loader in langchain that reads plain text(.txt) files and converts them into langchain document objects.

use case - 
1. ideal for loading chat logs, scraped text, transcript, code snippets, or any plain text data into a langchain pipeline.

Limitation - 
1. works only with .txt files

## PyPDFLoader - 
PyPDFLoader is a document loader in langchain used to load content from PDF files and convert each page into a Document object.
ex - 
[
    Document(page_content="Text from page 1", metadata={"page":0, "source":"file.pdf"}),
    Document(page_content="Text from page 2", metadata={"page":1, "source":"file.pdf"}),   
    ...
]

Limitations:
1. It uses the PyPDF library under the hood -- not greate with scanned PDFs or complex layouts.

## DirectoryLoader - 
DirectoryLoader is a document loader that lets you load multiple documents from a directory (folder) or files.
it loads all the files completely in the ram so it requires time and bigger ram size if directory contains numbers of files.

hence there is a concept of Lazy_load

## load() vs lazy_load()
1. load()
1.1 loads everything at once
1.2 returns a list of Document objects
1.3 loads all documents immediatly into memory.
1.4 best when:
                -> the number of documents is small
                -> you want everything loaded upfront
2. laze_load()
2.1 loads on demand
2.2 returns a generator of Document objects.
2.3 Documents are not all loaded at once. they are fetched one at a time as needed.
2.4 best when:
                -> you are dealing with large documents or lots of files.
                -> you want to stream processing (e.g. chunking, embedding) without using lots of memory.

## WebBaseLoader - 
WebBaseLoader is a document loader in langchain used to load and extract text content from web pages (URLs).
it uses BeautifulSoup under the hood to parse HTML and extract visible text.

When to use:
1. For blogs, news articles, public websites where the content is primarily text-based and static.

Limitations:
1. Doesn't handle JavaScript-heavy pages well (use SeleniumURLLoader for this).
2. Loads only static content (what's in the HTML, not what loads after the page renders).

## CSVLoader - 
CSVLoader is a document loader used to load CSV files into langchain document objects - one per row, by default.
