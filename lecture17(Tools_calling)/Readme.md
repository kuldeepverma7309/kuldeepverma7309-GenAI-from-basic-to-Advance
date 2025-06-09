# Tool Binding
- Tool Binding is the step where you register tools with a language model so that:
    - The LLM knows what tools are available
    - It knows what eact tool does (via the tool description)
    - It knows what input format to use (via the tool schema)

# Tool Calling
- Tool calling is the process where the LLM decides, during a conversation or task, that it needs to use a specific tool(function) - and generate a structured output with:
    - the name of the tool
    - and the arguments to call it with

*** LLM does not actually run the tool, it just suggests the tool and the input arguments. the actual execution is handled by LangChain or you. ***

# Tool Execution
- Tool Execution is the step where the actual python function (tool) is run using the input arguments that the LLM suggested during tool calling.

## in Simple words
- The LLM says:
    - "Hey, call the multiply tool with a=8 and b=7"
- Tool Execution is when you or LangChain actually run:
    - `multiply(a=8, b=7)`
    - and get the result back.


# InjectedToolArg: is a special type of tool argument that allows you to inject the output of one tool into another tool call.