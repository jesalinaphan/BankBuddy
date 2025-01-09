from fastapi import APIRouter
from app.ai.ai_model import ask_finance_assistant

router = APIRouter()

@router.post("/ask")
def ask_llm(query: str):
    response = ask_finance_assistant(query)
    return {"answer": response}
