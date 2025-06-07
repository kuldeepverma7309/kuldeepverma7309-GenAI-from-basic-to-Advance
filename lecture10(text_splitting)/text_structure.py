from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """Chennai Super Kings (CSK) is one of the most successful teams in IPL history, known for their consistent performances and loyal fan base. Led by MS Dhoni, CSK has won multiple titles and is famous for its strong team spirit and finishing abilities.

Royal Challengers Bangalore (RCB) is a team packed with star players and explosive batting line-ups. Despite reaching the finals several times in past but in 2025 RCB own their first IPL trophy. The team enjoys massive support, especially for players like Virat Kohli and AB de Villiers.

Mumbai Indians (MI) have set a benchmark in the IPL with their record number of championship wins. MI is known for its balanced squad, strong leadership under Rohit Sharma, and the ability to perform under pressure. Their rivalry with other top teams makes every match exciting.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,  # Fixed size of 100 characters for length-based splitting
    chunk_overlap=0,  # No overlap for length-based splitting
    separators=["\n\n", "\n", " ", ""]  # Using various separators to avoid cutting words in half
)

chunks = splitter.split_text(text)
print("Text splitting result:")
for i, chunk in enumerate(chunks):
    print(f"Chunk {i + 1}: {chunk}")