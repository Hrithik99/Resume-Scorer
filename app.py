import streamlit as st
import openai
import json
from utils.text_processing import extract_resume_text
from utils.scoring import get_job_relevance_score


# Streamlit UI
st.set_page_config(page_title="Resume vs Job Description Matcher", layout="wide")
st.title("📄 Resume vs Job Description Matcher")


# File Upload (Resume)
st.subheader("📤 Upload Resume (PDF or DOCX)")
uploaded_resume = st.file_uploader("Choose a resume file", type=["pdf", "docx"])

# Job Information Inputs
st.subheader("📝 Job Information")
job_title = st.text_input("💼 Job Title")
#company_name = st.text_input("🏢 Company Name")
job_description = st.text_area("📜 Paste Job Description Here", height=200)

# Process Resume
if st.button("🚀 Analyze Resume & Match"):
    if uploaded_resume and job_description:
        try:
                     
            
            # Extract structured resume content
            resume_text = extract_resume_text(uploaded_resume)

            # Display Raw Resume Text
            st.subheader("📑 Raw Resume Text")
            st.text(resume_text["Raw_Text"])
            # Get job relevance score using OpenAI
            score, reasoning = get_job_relevance_score(job_title, job_description, resume_text)

            # Display the Results
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
        st.warning("⚠️ Please upload a resume, enter job details, and provide your OpenAI API key.")

