text = """
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. the sum was bright and the air smelled of earth and fresh grass. The Indian Premier League (IPL) was in full swing, with teams battling it out for the championship. Chennai Super Kings (CSK) and Royal Challengers Bangalore (RCB) were among the top contenders, showcasing their skills and strategies on the cricket field.
Terrorism is a big problem in India, with various groups trying to disrupt peace and stability. The government is working hard to combat this issue, but it remains a significant challenge. The people of India are resilient and united in their efforts to overcome these challenges, whether in agriculture, sports, or security.
"""

from langchain_text_splitters import SemanticChunker
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

semantic_chunker = SemanticChunker(
    embeddings=embedding_model,
    breakpoint_threshold_type="percentile",
    breakpoint_threshold_amount=95,  # higher → larger chunks
)

chunks = semantic_chunker.split_text(my_large_text)