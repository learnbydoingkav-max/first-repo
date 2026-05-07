# ============================================================
# Tweet Generator - Main Application
# A Streamlit app that generates tweets using Google's Gemini
# AI model, orchestrated through LangChain.
# ============================================================
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain import LLMChain
from langchain_core.prompts import PromptTemplate
# Page Configiration 
st.set_page_config(page_title="Tweet Generator")
st.header("Tweet generator")
st.subheader("Generate tweets using Generative AI")
                   
#Secret key name:
GOOGLE_API_KEY
api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("Please ass GOOGLE_API_KEY to your Streamlit Secrets."
             st.stop()

# Initialize model and chain
# Note: Ensure "gemini-3.1-flash-lite-preview" is available in your region
#Initializing Google's Gemini Model
gemini_model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview", google_api_key=api_key)


import os

os.environ['GOOGLE_API_KEY'] = "AIzaSyC5-iqYz_4vn-LlFWgUDjW_zbvMxLa9ZJM"

#create promt template for generating tweets

tweet_template = "Give me {number} tweets on {topic}"

tweet_prompt = PromptTemplate.from_template(tweet_template)



#Create LLM chain using the promt template and model
tweet_chain = tweet_prompt | gemini_model

#Example of using the LLM chain
response = tweet_chain.invoke({"number" : 5, "topic" : "wars in Middle East"})



topic = st.text_input("Topic")
number = st.number_input("Number of tweets", min_value = 1, max_value = 10, value = 1, step = 1)
if st.button("Generate"):
    response = tweet_chain.invoke({"number": number, "topic": topic})
    st.write(response.content)
