import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_score_valid_cpf():
    response = client.get("/score/?cpf=12345678901")
    assert response.status_code == 200
    data = response.json()
    assert data["cpf"] == "12345678901"
    assert 300 <= data["score"] <= 950
    assert data["faixa"] in ["baixo", "médio", "bom", "excelente"]

def test_score_invalid_cpf_format():
    response = client.get("/score/?cpf=11111111111")
    assert response.status_code == 400
    assert response.json()["detail"] == "CPF inválido"

def test_score_missing_cpf():
    response = client.get("/score/")
    assert response.status_code == 422  # FastAPI retorna 422 para query param obrigatório faltando
