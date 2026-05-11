import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain import LLMChain
#from langchain_core.prompts import PromptTemplate
# Streamlit UI
st.title("B1 German Tutor 🇩🇪")

question = st.text_input("Ask your German question")

#Secret key name: GOOGLE_API_KEY
api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("Please ass GOOGLE_API_KEY to your Streamlit Secrets.")
    st.stop()

# Initialize model and chain
# Note: Ensure "gemini-3.1-flash-lite-preview" is available in your region
#Initializing Google's Gemini Model
gemini_model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview", google_api_key=api_key)

if st.button("Submit"):

    prompt = f"""
    You are a friendly German B1 tutor.
    
    Help the student learn German.
    Explain simply.
    Correct mistakes politely.
    
    Student question:
    {question}
    """

    response = model.generate_content(prompt)

    st.write(response.text)
