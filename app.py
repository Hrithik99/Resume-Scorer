import streamlit as st
import openai
import os
from utils.text_processing import extract_resume_text
from utils.scoring import get_job_relevance_score

from dotenv import load_dotenv

# Manually load `.env` file using absolute path
env_path = os.path.abspath("Config.env")
print(f"Loading .env from: {env_path}")  # Debugging print

load_dotenv(env_path)

# Fetch API key
api_key = os.getenv("OPENAI_API_KEY")



    
# Streamlit UI Configuration
st.set_page_config(page_title="Resume vs Job Description Matcher", layout="wide")
st.title("📄 Resume vs Job Description Matcher")

# OpenAI API Key Input
# If API key is not found, prompt user for input
if not api_key:
    st.subheader("🔑 Enter OpenAI API Key")
    api_key = st.text_input("🔐 OpenAI API Key", type="password")
else:
    # Store API key as a hidden input
    st.text_input("🔐 OpenAI API Key", value="●●●●●●●●●●", type="password", disabled=True)

# Store API Key in Session State (So it persists)
if api_key:
    st.session_state["OPENAI_API_KEY"] = api_key
    openai.api_key = api_key  # Set the API key for OpenAI client

# File Upload (Resume)
st.subheader("📤 Upload Resume (PDF or DOCX)")
uploaded_resume = st.file_uploader("Choose a resume file", type=["pdf", "docx"])

# Job Information Inputs
st.subheader("📝 Job Information")
job_title = st.text_input("💼 Job Title")
job_description = st.text_area("📜 Paste Job Description Here", height=200)

# Process Resume and Analyze
if st.button("🚀 Analyze Resume & Match"):
    if not api_key:
        st.warning("⚠️ Please enter your OpenAI API key.")
    elif uploaded_resume and job_description:
        try:
            # Extract raw resume text
            resume_text = extract_resume_text(uploaded_resume)

            # Get job relevance score using OpenAI
            score, reasoning = get_job_relevance_score(job_title, job_description, resume_text, api_key)

            # Display Results
            st.subheader("📊 Match Score & Analysis")
            if isinstance(score, int):
                st.markdown(f"### **🔥 Relevance Score: `{score}/10`**")
            else:
                st.warning("⚠️ Could not extract a score. See explanation below.")

            st.markdown("### 📌 **GPT-4 Job Fit Analysis:**")
            st.write(reasoning)

        except Exception as e:
            st.error(f"❌ An error occurred: {e}")

    else:
        st.warning("⚠️ Please upload a resume and enter job details.")
