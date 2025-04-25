# app.py
import os
import asyncio
from typing import List

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

# Carrega .env
load_dotenv()

API_TOKEN = os.getenv("PANDASCORE_TOKEN")
if not API_TOKEN:
    raise RuntimeError("PANDASCORE_TOKEN não definido!")

BASE_MATCHES_URL = "https://api.pandascore.co/csgo/matches"

app = FastAPI(title="FURIA CS Oracle API")

# 1) CORS — ajuste os domínios conforme seu front-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://seu-frontend.com"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# 2) Modelo de requisição
class MatchQuery(BaseModel):
    ids: List[int]

# 3) Função de consulta em batch


# 4) Endpoint POST para o front-end
@app.post("/matches/info")
async def matches_info(query: MatchQuery):
    """
    Recebe JSON { "ids": [123, 456, 789] }
    Retorna: { "matches": [ {...}, {...} ] }
    """
    partidas = await get_matches_by_ids(query.ids)
    # Opcional: aqui você pode filtrar só os campos que importa para o front
    resultado = []
    for m in partidas:
        resultado.append({
            "id": m["id"],
            "name": m["name"],
            "scheduled_at": m["scheduled_at"],
            "opponents": [
                opp["opponent"]["name"] for opp in m.get("opponents", [])
            ],
            # adicione outros campos que precisar...
        })
    return {"matches": resultado}

# 5) Rodando com Uvicorn
# uvicorn app:app --reload --host 0.0.0.0 --port 8000
