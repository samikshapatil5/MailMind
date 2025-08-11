import smtplib
import streamlit as st
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(recipient, body):
    try:
        sender_email = st.secrets["groq"]["SENDER_EMAIL"]
        sender_password = st.secrets["groq"]["EMAIL_PASSWORD"]
        smtp_server = st.secrets["groq"].get("SMTP_SERVER", "smtp.gmail.com")
        smtp_port = st.secrets["groq"].get("SMTP_PORT", 587)

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient
        message['Subject'] = "Response To Your Email"
        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)

        return True
    except Exception as e:
        print("Error sending email:", e)
        return False
