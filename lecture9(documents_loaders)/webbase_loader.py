from langchain_community.document_loaders import WebBaseLoader

url = "https://python.langchain.com/v0.1/docs/modules/data_connection/document_loaders/"

loader = WebBaseLoader(url)
docs = loader.load()
print(docs[0].page_content)
print(len(docs))