# ============================================================
# Tweet Generator - Main Application
# A Streamlit app that generates tweets using Google's Gemini
# AI model, orchestrated through LangChain.
# ============================================================
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain import LLMChain
from langchain_core.prompts import PromptTemplate

import streamlit as st

import os

os.environ['GOOGLE_API_KEY'] = "AIzaSyC5-iqYz_4vn-LlFWgUDjW_zbvMxLa9ZJM"

#create promt template for generating tweets

tweet_template = "Give me {number} tweets on {topic}"

tweet_prompt = PromptTemplate.from_template(tweet_template)

#Initializing Google's Gemini Model
gemini_model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview")

#Create LLM chain using the promt template and model
tweet_chain = tweet_prompt | gemini_model

#Example of using the LLM chain
response = tweet_chain.invoke({"number" : 5, "topic" : "wars in Middle East"})

import streamlit as st
st.header("tweet generator")
st.subheader("Generate tweets using Generative AI")
topic = st.text_input("Topic")
number = st.number_input("Number of tweets", min_value = 1, max_value = 10, value = 1, step = 1)
if st.button("Generate"):
    response = tweet_chain.invoke({"number": number, "topic": topic})
    st.write(response.content)
