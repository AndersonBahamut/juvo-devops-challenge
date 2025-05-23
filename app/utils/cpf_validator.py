# app/utils/cpf_validator.py

import re

def is_valid_cpf(cpf: str) -> bool:
    cpf = re.sub(r'\D', '', cpf)
    return len(cpf) == 11 and cpf.isdigit()
