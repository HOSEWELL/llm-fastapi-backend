# Gemini-Powered Q&A App (FastAPI + Gemini)

This project is part of a technical assessment to build a modern full-stack application that:
- Takes user questions,
- Integrates with an LLM (Gemini by Google),
- Returns structured responses via API.

## 💡 Example Use Case

**Question:**  
_“What documents do I need to travel from Kenya to Ireland?”_

**Answer:**  
The app returns visa requirements, passport details, and travel advisories — powered by Gemini AI.

---

## 🔧 Tech Stack

- **Backend:** FastAPI
- **LLM:** Gemini (Google Generative AI)
- **Styling/Frontend:** To be added (Next.js + TailwindCSS)

---

## 🚀 Getting Started Locally

### 1. Clone the repo
```bash
git clone https://github.com/your-username/llm-fastapi-backend.git
cd llm-fastapi-backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
Create a .env file in the root:
inside .env
GEMINI_API_KEY=your_google_api_key_here
Run server
uvicorn app.main:app --reload
'''bash
#### 📦 API Usage

POST /ask
{
  "question": "What documents do I need to travel to the USA from Kenya?"
}
📁 Folder Structure
app/
├── main.py
└── llm_service.py
.env
requirements.txt
README.md
