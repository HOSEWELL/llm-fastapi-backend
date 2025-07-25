from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.llm_service import get_answer_from_gemini
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost:3000",  
    "https://llm-frontend-woad.vercel.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask_question(q: Question):
    answer = get_answer_from_gemini(q.question)
    return {"answer": answer}
