import openai
import re

def get_job_relevance_score(job_title, job_description, master_resume, api_key):
    """Rates job relevance out of 10 using OpenAI API (v1.0+) with user-provided API key."""

    # ✅ Initialize OpenAI client dynamically with the API key
    client = openai.OpenAI(api_key=api_key)

    prompt = f"""
    You are an expert technical recruiter analyzing a candidate's resume against a job description.
    Your task is to:
    1. **Assess the candidate's resume** against the job description.
    2. **Provide a job relevance score (out of 10)** with an explanation.

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
    3. **Passion Towards Work (0-2 points)** – Does the candidate's background and personal projects show a deep interest in the {job_title} role?
    4. **Role-Specific Expertise (0-2 points)** – Does the candidate demonstrate deep domain expertise?

    ---
    ### **🔍 Output Format:**
    **Relevance Score:** X/10  

    **Reasoning:** (A deep analysis of why the score was assigned and key pointers on what is missing. Also, add a brief conclusion on areas where the candidate should improve to be a better fit for the role.)  

    ---
    **Now, analyze the candidate’s resume and provide ONLY the Relevance Score and Reasoning. DO NOT include extracted resume sections in the output.**
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
