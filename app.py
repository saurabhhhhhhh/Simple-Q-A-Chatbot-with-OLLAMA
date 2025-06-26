import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import os
from dotenv import load_dotenv
load_dotenv()


os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"]="CHATBOT Q&NA"


prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant.please response to the user query"),
        ("user","question:{question}")
    ]
)


def genrate_response(question,engine,temperature,max_tokens):

    llm=Ollama(model=engine)
    output_parser=StrOutputParser()
    chain=prompt | llm | output_parser
    answer=chain.invoke({"question":question})
    return answer

engine=st.sidebar.selectbox("Select an engine", ["llama3.2", "mistral", "gemma3"])

temperature=st.sidebar.slider("temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("max tokens",min_value=50,max_value=300,value=150)

st.write("go ahead and ask your question")
user_input=st.text_input("you:")

if user_input:
    response=genrate_response(user_input,engine,temperature,max_tokens)
    st.write(response)

else:
    st.write("Please enter a question to get a response.")
