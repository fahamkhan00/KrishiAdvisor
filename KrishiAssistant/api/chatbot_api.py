# api/chatbot_api.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
from app import main  # wraps RAG + translation

app = FastAPI()

class Query(BaseModel):
    query: str

@app.post("/ask")
def ask(query: Query):
    response = main(query.query)
    return {"answer": response}
