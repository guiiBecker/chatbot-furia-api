#ARQUIVO PARA BUSCA DE TIMES, FIZ DESTA MANEIRA POIS QUERO USAR POSTERIORMENTE PARA PROJETO POSSOAL

import os
import asyncio
import httpx
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_TOKEN = os.getenv("PANDASCORE_TOKEN")
if not API_TOKEN:
    raise RuntimeError("PANDASCORE_TOKEN não definido. Verifique seu .env ou exportação.")

#BASE_URL = "https://api.pandascore.co/csgo/teams"
#BASE_URL = "https://api.pandascore.co/r6siege/teams"

async def get_all_teams():
    teams = []
    page = 1
    per_page = 100
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    async with httpx.AsyncClient() as client:
        while True:
            resp = await client.get(
                BASE_URL,
                headers=headers,
                params={"page": page, "per_page": per_page}
            )
            # Em caso de 401 você verá esta mensagem no console
            if resp.status_code == 401:
                print("401 Unauthorized:", resp.text)
                raise RuntimeError("Token inválido ou não autorizado pela PandaScore.")
            resp.raise_for_status()

            batch = resp.json()
            if not batch:
                break

            teams.extend(batch)
            page += 1

    return teams

async def main():
    todos_os_times = await get_all_teams()
    print(f"Foram encontrados {len(todos_os_times)} times.")
    for t in todos_os_times:
        print(f"{t['id']} — {t['name']}")

if __name__ == "__main__":
    asyncio.run(main())
