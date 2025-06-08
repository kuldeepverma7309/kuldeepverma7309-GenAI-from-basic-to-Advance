# Plan of Action: here we are building youtube chatbot using langchain and youtube transcript api

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound, VideoUnavailable
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

# =======================================Indexing========================================= 
# step 1: Fetching the transcript of a YouTube video
def fetch_youtube_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([entry['text'] for entry in transcript_list])
        return transcript
    except TranscriptsDisabled:
        print("Transcripts are disabled for this video.")
    except NoTranscriptFound:
        print("No transcript found for this video.")
    except VideoUnavailable:
        print("The video is unavailable.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None
transcript = fetch_youtube_transcript("gyOFdkWx7j0")
# print(transcript)   

if transcript is None:
    print("Failed to fetch transcript. Exiting.")
    exit(1)

# step 2: Splitting the transcript into smaller chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.create_documents([transcript])

# step 3: Creating embeddings for the chunks
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = FAISS.from_documents(chunks, embeddings)

# ========================================Retrieval=========================================

# step 4: Setting up the retriever
retriever = vector_store.as_retriever(search_type="similarity",search_kwargs={"k": 3})

# response = retriever.invoke("What is the main topic of the video?")
# print(f"Response: {response}")

# ========================================Augmentation=========================================

# step 5: Setting up the language model
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct:free",
    openai_api_base="https://openrouter.ai/api/v1",
)

# step 6: Creating a prompt template
prompt_template = PromptTemplate(
    template="You are a helpful assistant. Answer the question based on the provided transcript context. it the context is insufficient, just say i don't know.\n\nContext:\n{context}\n\nQuestion: {question}",
    input_variables=["context", "question"]
)

question = "What is the main topic of the video?"
retrived_docs = retriever.invoke(question)

context_text = "\n".join([doc.page_content for doc in retrived_docs])

final_prompt = prompt_template.invoke({"context": context_text, "question": question})

# =========================================Response Generation=========================================

# answer = llm.invoke(final_prompt)
# print(f"Question: {question}")
# print(f"Answer: {answer.content}")

# =========================================End of Code=========================================

# Now Implementing above code using chain
# there will be two chains one is parallel chain for retriever context and question and another sequential chain for prompt template and llm

def format_docs(retrieved_docs):
    return "\n".join([doc.page_content for doc in retrieved_docs])

parallel_chain = RunnableParallel(
    {
        'context': retriever | RunnableLambda(format_docs),
        'question': RunnablePassthrough()
    }
)

parser = StrOutputParser()
prompt = prompt_template
# parallel_chain_result = parallel_chain.invoke(question)

main_chain = parallel_chain | prompt | llm | parser

final_chain_response = main_chain.invoke(question)
print(f"Question: {question}")
print(f"Answer: {final_chain_response}")