import streamlit as st
from openai import OpenAI

# Load API key from Streamlit secrets
groq_api_key = st.secrets["groq"]["api_key"]

# Groq-compatible client
client = OpenAI(
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1"
)

def generate_email_response(email_text, tone):
    prompt = f"""
You are an AI assistant. Write a reply to the following email using a {tone.lower()} tone:

Email:
{email_text}

Reply:
"""
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",  # You can change to other Groq-supported models
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"❌ Groq API Error: {str(e)}")
        return "[ERROR] Could not generate email response."
