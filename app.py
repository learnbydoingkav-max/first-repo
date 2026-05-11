import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI
st.title("B1 German Tutor 🇩🇪")

question = st.text_input("Ask your German question")

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