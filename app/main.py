from fastapi import FastAPI
from app.routes.score import router as score_router

app = FastAPI()

# Registra a rota /score
app.include_router(score_router)
