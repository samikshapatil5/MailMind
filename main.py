import streamlit as st
from agents.email_agent import generate_email_response
from utils.email_sender import send_email

# Page setup
st.set_page_config(page_title="Auto Email Responder", layout="wide")
st.title("📧 MailMind: Brains Behind Every Send")

# Input fields
email_text = st.text_area(" Paste the email content you received:", height=300)
recipient_email = st.text_input(" Recipient Email Address")
tone = st.selectbox(" Select response tone", ["Professional", "Friendly", "Apologetic", "Persuasive"])

# Button to trigger response and sending
if st.button(" Generate & Send Email"):
    if not recipient_email.strip():
        st.warning(" Please enter the recipient's email address.")
    elif not email_text.strip():
        st.warning("Please paste some email content.")
    else:
        with st.spinner("Generating and sending email..."):
            try:
                # Generate response using Gemini
                response = generate_email_response(email_text, tone)

                # Send email via SMTP
                send_status = send_email(recipient_email, response)

                # Display generated response
                st.subheader("AI-Generated Response")
                st.markdown(response)

                # Email sending status
                if send_status:
                    st.success(f"Email sent successfully to `{recipient_email}`.")
                else:
                    st.error("Failed to send the email. Please check the logs or credentials.")

            except Exception as e:
                st.error(f"Unexpected error: {e}")
