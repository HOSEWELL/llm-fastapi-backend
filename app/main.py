from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.llm_service import get_answer_from_gemini

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
def ask_question(payload: QuestionRequest):
    answer = get_answer_from_gemini(payload.question)
    if "Error from Gemini" in answer:
        raise HTTPException(status_code=500, detail=answer)
    return {"answer": answer}
