import streamlit as st
import google.generativeai as genai

# Configure Gemini API with your key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Function to generate email response
def generate_email_response(email_text, tone):
    prompt = f"""
You are an AI assistant. Write a reply to the following email using a {tone.lower()} tone.

Email:
{email_text}

Reply:
"""
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Gemini API Error: {str(e)}")
        return "[ERROR] Could not generate email response."
