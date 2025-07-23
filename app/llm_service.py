import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not set in environment variables")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

def get_answer_from_gemini(question: str) -> str:
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"Error from Gemini: {e}"
