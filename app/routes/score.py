from fastapi import APIRouter, HTTPException
from app.services.score_service import get_score, faixa_score
from app.utils.cpf_validator import is_valid_cpf

router = APIRouter(prefix="/score", tags=["score"])

@router.get("/{cpf}")
def consultar_score(cpf: str):
    if not is_valid_cpf(cpf):
        raise HTTPException(status_code=400, detail="CPF inválido")

    score = get_score(cpf)
    faixa = faixa_score(score)

    return {"cpf": cpf, "score": score, "faixa": faixa}
