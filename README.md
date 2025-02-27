# 📄 Resume Matcher – AI-Powered Job Fit Scorer

🚀 **Resume Matcher** is a **Streamlit-based AI application** that evaluates a candidate's resume against a given job description using **GPT-4**. 
It provides a **relevance score (0-10)** and detailed feedback on how well the resume aligns with the job requirements.

---

## **🌟 Features**
✅ **AI-Powered Resume Scoring** – Uses GPT-4 to analyze job relevance.  
✅ **Raw Resume Text Extraction** – Supports **PDF & DOCX** resumes.  
✅ **Structured Job Fit Analysis** – Evaluates **Skills, Experience, Industry Fit, and Expertise**.  
✅ **User-Friendly UI** – Built with **Streamlit** for an interactive experience.  
✅ **Deployable on AWS EC2** – Runs efficiently on **Cloud Servers**.  

---

## **🛠️ Tech Stack**
- **Python 3.9+**
- **Streamlit** (Frontend UI)
- **OpenAI GPT-4 API**
- **PDFMiner** (PDF Parsing)
- **python-docx** (DOCX Parsing)
- **AWS EC2 (Ubuntu 22.04)** (Deployment)

---

## **📥 Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Hrithik99/resume-matcher.git
cd resume-matcher

2️⃣ Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
Activate it:

Windows (PowerShell):
powershell
Copy
Edit
venv\Scripts\Activate.ps1
Mac/Linux:
bash
Copy
Edit
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up OpenAI API Key
Create a .env file in the project root:

bash
Copy
Edit
echo "OPENAI_API_KEY=your-api-key-here" > .env
Replace "your-api-key-here" with your actual OpenAI API key.

🚀 Running the Application
bash
Copy
Edit
streamlit run app.py
🔗 Open the app in your browser at:
👉 http://localhost:8501

🛠️ Project Structure
bash
Copy
Edit
resume-matcher/
│── app.py                  # Main Streamlit application
│── requirements.txt         # Required Python dependencies
│── .gitignore               # Git ignore rules
│── .env                     # Environment variables (not pushed to GitHub)
│── utils/
│   ├── text_processing.py   # Handles resume text extraction
│   ├── scoring.py           # Calls OpenAI API for job matching
│── README.md                # Project documentation (This file)
📌 How It Works
1️⃣ Upload a Resume (PDF or DOCX).
2️⃣ Enter Job Title, Company Name, and Job Description.
3️⃣ Click "Analyze Resume & Match" – The app extracts raw text and sends it to GPT-4 for analysis.
4️⃣ View the Relevance Score & LLM Explanation.

📡 Deployment on AWS EC2
1️⃣ Launch an EC2 Instance (Ubuntu 22.04)
Use t2.micro (Free Tier) or t3.small for better performance.
Open ports 22 (SSH), 80 (HTTP), and 8501 (Streamlit).
2️⃣ Connect to Your EC2 Instance
bash
Copy
Edit
ssh -i your-key.pem ubuntu@your-ec2-public-ip
3️⃣ Install Dependencies
bash
Copy
Edit
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip -y
pip install streamlit openai python-dotenv pdfminer.six python-docx
4️⃣ Clone & Run the App
bash
Copy
Edit
git clone https://github.com/Hrithik99/resume-matcher.git
cd resume-matcher
streamlit run app.py --server.port 8501 --server.enableCORS false --server.enableXsrfProtection false
5️⃣ Access Your App
🔗 Open http://your-ec2-public-ip:8501 in your browser.

🔧 Troubleshooting
If API key is missing, make sure .env is correctly loaded.
If Streamlit is not accessible, ensure port 8501 is open in EC2 security rules.
If dependencies fail, run:
bash
Copy
Edit
pip install -r requirements.txt --upgrade
👨‍💻 Contribution
Contributions are welcome! To contribute:

Fork the Repo & create a new branch.
Implement your changes & test locally.
Create a Pull Request (PR) on GitHub.
📄 License
This project is MIT Licensed – free to use and modify.

📞 Contact
For any issues or suggestions, feel free to reach out:

📧 Email: hrithiksarda4@gmail.com
💼 LinkedIn: [Your LinkedIn](https://www.linkedin.com/in/hrithiksarda/)
