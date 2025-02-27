import openai
import os
import re
from dotenv import load_dotenv

env_path = os.path.abspath("Config.env")
load_dotenv(env_path)
api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=api_key)

def get_job_relevance_score(job_title, job_description, master_resume):
    """Rates job relevance out of 10 using OpenAI API (v1.0+)."""

    prompt = f"""
    You are an expert technical recruiter analyzing a candidate's resume against a job description.
    Your task is to:
    1. **Extract structured sections** from the raw resume text (Experience, Skills, Education, Projects, Certifications, Summary).
    2. **Compare these extracted sections** with the given job description.
    3. **Provide a detailed job relevance score (out of 10)** with an explanation.

    **🔹 Job Details:**
    - **Job Title:** {job_title}
    - **Job Description:** {job_description}

    **🔹 Candidate's Resume (Raw Text Input):**
    ```
    {master_resume}
    ```

    ---
    ### **🎯 Evaluation Criteria (Score Breakdown)**
    1. **Skill Match (0-3 points)** – Does the candidate’s skillset align with the job requirements?
    2. **Experience Relevance (0-3 points)** – How well does the candidate's past experience match the role?
    3. **Industry Fit (0-2 points)** – Does the candidate's background align with the company's industry?
    4. **Role-Specific Expertise (0-2 points)** – Does the candidate demonstrate deep domain expertise?

    ---
    ### **🔍 Output Format:**
    **Relevance Score:** X/10  
    **Extracted Resume Sections:**  
    - **Experience:** (Summarized list of roles & projects)  
    - **Skills:** (Extracted technical and soft skills)  
    - **Education:** (Relevant degrees and certifications)  
    - **Projects:** (Key projects mentioned)  
    - **Certifications:** (Relevant certifications)  

    **Reasoning:** (Brief explanation of why the score was assigned.)  

    ---
    **Now, analyze the candidate’s resume and provide a structured response.**
    """


    try:
        response = client.chat.completions.create(  # ✅ NEW METHOD (v1.0+)
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert recruiter evaluating job candidates."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5
        )

        output_text = response.choices[0].message.content  # ✅ NEW WAY TO ACCESS RESPONSE

        # Extract the relevance score using regex for reliability
        match = re.search(r"\*\*Relevance Score:\*\* (\d+)/10", output_text)
        score = int(match.group(1)) if match else "N/A"

        return score, output_text

    except Exception as e:
        return "Error", f"An error occurred while fetching the relevance score: {str(e)}"
