from fastapi import FastAPI, Depends
from app.auth.jwt_handler import verify_token
from app.services.l2c_service import l2c_decision_engine

app = FastAPI()

@app.post("/l2c/intelligence")
def get_decision(query: str, token: str):
    verify_token(token)
    embedding = [0.1] * 384
    return l2c_decision_engine(query, embedding)
