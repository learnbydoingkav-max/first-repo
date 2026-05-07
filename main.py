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
                   
#Secret key name: GOOGLE_API_KEY
api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("Please ass GOOGLE_API_KEY to your Streamlit Secrets.")
    st.stop()

# Initialize model and chain
# Note: Ensure "gemini-3.1-flash-lite-preview" is available in your region
#Initializing Google's Gemini Model
gemini_model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview", google_api_key=api_key)

#create promt template for generating tweets
tweet_template = "Give me {number} tweets on {topic}"
tweet_prompt = PromptTemplate.from_template(tweet_template)
#Create LLM chain using the promt template and model
tweet_chain = tweet_prompt | gemini_model

#UI Logic
topic = st.text_input("Topic", placeholder="Enter a topic...")
number = st.number_input("Number of tweets", min_value = 1, max_value = 10, value = 1)
if st.button("Generate"):
    if topic.strip():
        with st.spinner("Generating tweets..."):
            try:
                # This only runs when the button is clicked
                response = tweet_chain.invoke({
                    "number": number,
                    "topics": topic   # Corrected 'topic' to 'topics'
                })

                # Attempt to parse as JSON for formatted display, else write content
                try:
                    import json
                    parsed_content = json.loads(response.content)
                    st.json(parsed_content) # Display as formatted JSON
                except json.JSONDecodeError:
                    st.write(response.content) # Display as plain text

            except Exception as e:
                st.error(f"AI Error: {e}")

    # The 'else' block indentation is logically correct as provided.
    # It handles the case where 'topic' is empty after the 'Generate' button is clicked.
    else:
        st.warning("Please enter a topic first")
















    response = tweet_chain.invoke({"number": number, "topic": topic})
    
