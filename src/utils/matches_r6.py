import asyncio
import httpx
import json
from typing import List, Dict
from getToken import get_token  # importa a função que carrega o token

# constantes de filtro
TARGET_NAME = "FURIA"
TARGET_ID = 127596

BASE_URL = "https://api.pandascore.co/r6siege/matches/past"

async def fetch_all_past_matches(token: str) -> List[Dict]:
    headers = {"Authorization": f"Bearer {token}"}
    matches: List[Dict] = []
    page, per_page = 1, 100

    async with httpx.AsyncClient() as client:
        while True:
            resp = await client.get(
                BASE_URL,
                headers=headers,
                params={"page": page, "per_page": per_page}
            )
            resp.raise_for_status()
            data = resp.json()
            if not data:
                break
            matches.extend(data)
            page += 1

    return matches

async def get_matches_r6():
    # obtém o token via get_token()
    api_token = get_token()

    # busca e filtra as partidas
    all_matches = await fetch_all_past_matches(api_token)
    furia_matches: List[Dict] = []

    for match in all_matches:
        opponents = match.get("opponents", [])
        # verifica se FURIA participou
        if any(
            opp["opponent"]["name"].upper() == TARGET_NAME or
            opp["opponent"]["id"] == TARGET_ID
            for opp in opponents
        ):
            # extrai placares
            results = match.get("results", [])
            our = next((r for r in results if r.get("team_id") == TARGET_ID), None)
            other = next((r for r in results if r.get("team_id") != TARGET_ID), None)
            if not our or not other:
                continue

            our_score = our["score"]
            other_score = other["score"]

            # encontra o nome do adversário
            opponent_name = next(
                opp["opponent"]["name"]
                for opp in opponents
                if opp["opponent"]["id"] != TARGET_ID
            )

            # determina resultado
            if our_score > other_score:
                outcome = "Venceu"
            elif our_score < other_score:
                outcome = "Perdeu"
            else:
                outcome = "Empatou"

            # monta o JSON de saída
            furia_matches.append({
                "id": match["id"],
                "opponent": opponent_name,
                "score": f"{our_score}-{other_score}",
                "result": outcome,
                "date": match.get("begin_at")
            })

    # imprime o total de partidas filtradas
    print(f"Total de partidas da furia buscadas: {len(furia_matches)}")

    # gera e imprime o JSON
    print("json gerado")
    print(json.dumps(furia_matches, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    asyncio.run(get_matches_r6())
