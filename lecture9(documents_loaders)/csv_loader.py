from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="social_media_posts.csv",
)

docs = loader.load()
print(docs[0].page_content)
print(len(docs))