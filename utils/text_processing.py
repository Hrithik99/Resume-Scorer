import pdfminer.high_level
from docx import Document
import io

def extract_text_from_pdf(file):
    """Extracts raw text from a PDF file (reads directly from memory)."""
    return pdfminer.high_level.extract_text(file)

def extract_text_from_docx(file):
    """Extracts raw text from a DOCX file (reads directly from memory)."""
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text(uploaded_file):
    """Extracts text from a resume file (PDF or DOCX) uploaded in Streamlit."""
    
    file_extension = uploaded_file.name.split(".")[-1].lower()

    if file_extension == "pdf":
        return extract_text_from_pdf(uploaded_file)
    elif file_extension == "docx":
        return extract_text_from_docx(uploaded_file)
    else:
        raise ValueError("Unsupported file format. Please upload a PDF or DOCX file.")

def extract_resume_text(file):
    """Extracts and returns raw resume text for LLM processing."""
    raw_text = extract_text(file)
    return {"Raw_Text": raw_text}

