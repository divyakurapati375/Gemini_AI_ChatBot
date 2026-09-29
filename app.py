import streamlit as st
from dotenv import load_dotenv
import os
from google import  genai
with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
load_dotenv()
api_key = os.getenv("GENAI_API_KEY")
client = genai.Client(api_key=api_key)
st.set_page_config(page_title="Gemini AI Chatbot",layout="centered")
st.title("Gemini AI Chatbot")
st.write("Ask gemini anything!")
prompt=st.text_area("Explain AI")
if st.button("generate response"):
    if prompt:
        with st.spinner("Gemini is thinking..."):
            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )
        st.success("Response generated!")
        st.write(response.text)
    else:
        st.error("Please enter a prompt to generate a response.")
