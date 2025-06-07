from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = """
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,  # Fixed size of 100 characters for length-based splitting
    chunk_overlap=0,  # No overlap for length-based splitting
)

chunks = splitter.split_text(text)
print("Text splitting result:")
for i, chunk in enumerate(chunks):
    print(f"Chunk {i + 1}: {chunk}")