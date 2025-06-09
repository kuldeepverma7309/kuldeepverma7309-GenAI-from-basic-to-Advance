from langchain_community.tools import DuckDuckGoSearchRun,ShellTool
from langchain_core.tools import tool
from langchain.tools import StructuredTool, BaseTool
from pydantic import BaseModel, Field
from typing import Type


# ========================================== DuckDuckGo Search Tool ==========================================
# search_tool = DuckDuckGoSearchRun()

# result = search_tool.invoke("What is LangChain?")
# print(result)

# ========================================== Shell tool ==========================================
# shell_tool = ShellTool()
# result = shell_tool.invoke("whoami")
# print(result)

# ========================================== Custom Tool ==========================================

# # step 1: Define the function
# def add_numbers(a, b):
#     """Add two numbers."""
#     return a + b

# # step 2: add type hints
# def add_numbers(a: int, b: int) -> int:
#     """Add two numbers."""
#     return a + b

# # step 3: add tool decorator. this tool decorator will convert the function into a tool that can be used in LangChain.
# @tool
# def add_numbers(a: int, b: int) -> int:
#     """Add two numbers."""
#     return a + b

# result = add_numbers.invoke({"a": 5, "b": 3})
# print(result)  # Output: 8
# print(add_numbers.description)  # Output: Add two numbers.
# print(add_numbers.name)  # Output: add_numbers
# print(add_numbers.args)

# ========================================== Structured Tool ==========================================
# class AddNumbersInput(BaseModel):
#     a: int = Field(required=True, description="The first number to add.")
#     b: int = Field(required=True, description="The second number to add.")

# def add_number_structured(a:int, b:int) -> int:
#     """Add two numbers."""
#     return a + b

# addition_tool = StructuredTool.from_function(
#     func=add_number_structured,
#     name="addNumbers",
#     description="Add two numbers",
#     args_schema=AddNumbersInput
# )

# result = addition_tool.invoke({'a':9, 'b':9})
# print(result)

# ================================== Using Base Tool class =======================================

# # arg schema using pydantic

# class MultiplyInput(BaseModel):
#     a: int = Field(required=True, description="The first number to add")
#     b: int = Field(required=True, description="The second number to add")

# class MultiplyTool(BaseTool):
#     name: str = "multiply"
#     description: str = "Multiply two numbers"

#     args_schema: Type[BaseModel] = MultiplyInput

#     def _run(self, a: int, b: int) -> int:
#         return a * b

# multiply_tool = MultiplyTool()

# result = multiply_tool.invoke({'a':3, 'b':3})

# print(result)
# print(multiply_tool.name)
# print(multiply_tool.description)

# print(multiply_tool.args)

# ================================== Toolkits =======================================
# Custom tools
@tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

class MathToolkit:
    def get_tools(self):
        return [add, multiply]
    
toolkit = MathToolkit()
tools = toolkit.get_tools()

for tool in tools:
    print(tool.name, "=>", tool.description)
    print("Example usage:", tool.invoke({"a": 2, "b": 3}))