import requests
from fastapi import FastAPI, Request
from auth import Auth
from joke import Joke
from logger import Logger
app = FastAPI()

@app.get("/joke")
async def root(request: Request):
    response = requests.get("https://api.chucknorris.io/jokes/random").json()
    Joke.from_dict(response)
    return Joke.from_dict(response)

app.add_middleware(Auth)
app.add_middleware(Logger, account_provider=Auth.get_account)

