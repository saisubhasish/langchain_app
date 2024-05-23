import os
import streamlit as st
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers.string import StrOutputParser



os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
#Langsmith tracking
os.environ['LANCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")

# Prompt Template

prompt = ChatPromptTemplate.from_messages([
    # Messages are represented as dictionaries
    ("system","You are a helpful assistant. Please response to the user queries!"),
    ("user", "content: {question}"),
])

# Streamlit framework
st.title("LangChain Demo with OpenAI API")
input_text = st.text_input("Ask your question")

#OpenAI LLM
llm = ChatOpenAI(model='gpt-3.5-turbo')
output_parser = StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))
