## Text Splitting
Text splitting is the process of breaking large chunks of text (like articles, pdfs, HTML pages or books) into smaller, manageable pieces (chunks) that an LLM can handle effectively.

## Overcoming model limitations
LLMs have a context window limit, which is the maximum number of tokens they can process at once. For example, GPT-3.5 has a context window of 4096 tokens, while GPT-4 has a context window of 8192 tokens. Text splitting helps to overcome this limitation by dividing large texts into smaller chunks that fit within the model's context window.

## Types of Text Splitting
1. **Length-based splitting**: This method divides text into chunks of a fixed number of tokens. It is simple but may cut off sentences or paragraphs, leading to loss of context. Example: splitting a text into chunks of 512 tokens each.
2. **Text Structure-based splitting**: This method uses the structure of the text (like paragraphs, headings, or sections) to create chunks. It preserves context better than length-based splitting. Example: splitting a text into chunks based on paragraphs or sections.
3. **Document-based splitting**: This method is used for splitting documents like python files, markdown files, or HTML files into smaller parts. It can be based on file structure or content. Example: splitting a markdown file into sections based on headings.
4. **Semantic splitting**: This method uses semantic analysis to create chunks based on the meaning of the text. It ensures that each chunk is coherent and contextually relevant, but it is more complex and computationally intensive. Example: using NLP techniques to identify key sentences or topics and create chunks based on them.


