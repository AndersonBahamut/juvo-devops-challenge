from pydantic import BaseModel, Field

class ScoreResponse(BaseModel):
    cpf: str = Field(..., description="Número do CPF (somente dígitos)")
    score: int = Field(..., ge=0, le=1000, description="Score de crédito entre 0 e 1000")
    faixa: str = Field(..., description="Classificação do score (baixo, médio, bom, excelente)")
