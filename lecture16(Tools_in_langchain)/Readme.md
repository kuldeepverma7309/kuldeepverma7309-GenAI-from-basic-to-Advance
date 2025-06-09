# What is a Tool?
- A Tool is just a python function (or API) that is packaged in a way the LLM can understand and call when needed.
- LLMs (like GPT) are great at:
    - Reasoning
    - Language generation
- But they can't do things like:
    - Access live data (Weather, Stock prices, etc.)
    - Do reliable math
    - Call APIs
    - Run code
    - Interact with databases
## its mean in simple words LLMs is like a human without hands and legs and tools are mechanism to give them hands and legs to do things.
# Tools in LangChain
- In LangChain there are two types of tools:
    - Build-in tools as to google search, command line, etc.
    - Custom tools that you can create to do specific tasks.

## How Tools fits into the Agent ecosystem
- An AI agent is an LLM-powered system that can autonomously think, decide and take actions using external tools or APIs TO achieve a specific goal.
- In simple words, an agent is combination of LLMs(Reasoning & Decision Making) and tools(Action).

## Built-in Tools
- A built-in tool is a tool that langchain already provides for you. it's pre built, production-ready, and requires minimal or no setup.
- You don't have to write the function logic yourself. You just import and use it.
    - Example
        - DuckDuckGoSearchRun -> Web Search via DuckDuckGo
        - WikipediaQueryRun -> Query Wikipedia
        - PythonREPLTool -> Run Python code
        - ShellTool -> Run shell commands
        - RequestGetTool -> Make HTTP GET requests
        - GmailSendMessageTool -> Send emails via Gmail
        - SlackSendMessageTool -> Post message to Slack
        - SQLDatabaseQueryTool -> Run SQL Queries

## Custom Tools
- A custom tool is a tool that you define yourself.
- when to use
    - you want to call your own function or API
    - you want to encapsulate business logic
    - you want to LLM to interact with your database, product, or app
- There are 3 ways to create custom tools:
    - using `@tool` decorator
    - using StructuredTool & Pydantic
    - Using BaseTool class

    ### StructuredTool: A structured tool in langchain is a special type of tool where the input to the tool follows a structured schema, typically defined using Pydantic model.

    ### BaseTool: A base tool is the abstract base class for all tools in langchain. it defines the core structure  and interface that any tool must follow, whether it's simple one-liner or a fully customized function. All other tool types like `@tool`, `StructuredTool` are built on top of this base class.

# Toolkits
- A toolkit is just a collection (bundle) of related tools that serve a comon purpost packaged together for convenience and resuability.
- In langchain:
    - A toolkit might be: GoogleDriveToolkit
    - And it can contain the following tools

        - GoogleDriveCreateFileTool -> Upload a file to Google Drive
        - GoogleDriveSearchTool -> Search for a file by name/content
        - GoogleDriverReadFileTool -> Read content of a file