# 🧠 API de Score de Crédito

Esta API retorna o **score de crédito** de uma pessoa com base no CPF informado. É uma API crítica, projetada para ser **resiliente, escalável e segura**.

---

## 🚀 Stack Utilizada

- **Python 3.11**
- **FastAPI** + Uvicorn
- **Docker Compose**
- **Pydantic** (validação)
- **pytest** + httpx (testes)
- **Boto3** (reservado para produção AWS)

---

## 🔧 Executando Localmente com Docker Compose

### Pré-requisitos

- Docker
- Docker Compose (versão V2 recomendada)

### Instruções

#### ✅ Docker Compose V2 (padrão atual):

```bash
docker compose up --build

Teste via http://localhost:8000/score/12345678909
Teste via bash curl http://localhost:8000/score/12345678909