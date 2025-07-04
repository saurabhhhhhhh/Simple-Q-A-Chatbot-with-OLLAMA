# Simple-Q-A-Chatbot-with-OLLAMA
A lightweight interactive Q&amp;A chatbot built using LangChain, Streamlit, and Ollama for running local LLMs like llama3, mistral, and gemma. This app allows users to ask natural language questions and get AI-generated answers from locally hosted models. Easily extendable, open-source, and great for experimenting with LLM pipelines.



# Local LLM Chatbot using Streamlit, LangChain, and Ollama

This project is a lightweight local chatbot application built using:

- LangChain for LLM orchestration and prompt handling
- Ollama for running local large language models (LLMs) such as `llama3`, `mistral`, and `gemma`
- Streamlit for an interactive user interface
- dotenv for managing environment variables securely

## Features

- Supports multiple local LLMs including `llama3`, `mistral`, and `gemma`
- Configurable temperature and maximum token limits
- Simple question-answer interface
- LangChain tracing support for debugging and observability

 
`python -m venv venv `
`venv\Scripts\activate`  # On Windows
or
`source venv/bin/activate`  # On macOS/Linux

# Install required dependencies
`pip install -r requirements.txt`

# Create a .env file in the project root 
- LANGCHAIN_API_KEY=your_langchain_api_key
- Enable LangChain Tracing (optional):
- LANGCHAIN_TRACING_V2=true
- LANGCHAIN_PROJECT=CHATBOT Q&NA

# Download Required Models via Ollama
`ollama pull llama3`
`ollama pull mistral`
`ollama pull gemma`

# Running the Application
`streamlit run app.py`


