import random

def get_score(cpf: str) -> int:
    return random.randint(0, 1000)

def faixa_score(score: int) -> str:
    if score < 400:
        return "Baixo"
    elif score < 700:
        return "Médio"
    else:
        return "Alto"