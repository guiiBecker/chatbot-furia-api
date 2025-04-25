
import os
from dotenv import load_dotenv, find_dotenv

def get_token():
    load_dotenv(find_dotenv())
    token = os.getenv("PANDASCORE_TOKEN")
    if not token:
        raise RuntimeError("PANDASCORE_TOKEN não definido!")

    return token


if __name__ == "__main__":
    get_token()
