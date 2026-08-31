import os
from dotenv import load_dotenv

# Load .env when running locally
load_dotenv()

# Try environment variable first
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# If not found, try Streamlit secrets
if not GROQ_API_KEY:
    try:
        import streamlit as st
        GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")
    except Exception:
        GROQ_API_KEY = None

# Stop the application if the key is still missing
if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY is not configured. "
        "Add it to your .env file locally or Streamlit Secrets when deployed."
    )
