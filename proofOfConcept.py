from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Subscription Keeper")

class Subscription(BaseModel):
    id: int
    name: str
    cost: float
    shared: bool

subscriptions = [
    Subscription(id=1, name="Netflix", cost=15.99, shared=True),
    Subscription(id=2, name="Spotify", cost=11.99, shared=False),
]

@app.get("/subscriptions")
async def get_subscriptions():
    return subscriptions
