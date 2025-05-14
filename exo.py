from fastapi import FastAPI, Query, Path, Body

from typing import Optional
from pydantic import BaseModel


fake_users_db = [{"user_name": "John"}, {"user_name": "Doh"}, {"user_name": "Baz"}]

class Users(BaseModel):
    name: str
    first_name: str
    date_of_birth: int
    email: Optional[str] = None

user_db = []

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Bienvenue sur mon API fastAPI"}


@app.get("/users/")
async def list_users(skip: int = 0, limit: int = 10):
    return user_db[skip : skip + limit]

@app.get("/users/{user_id}")
async def read_user(user_id: int):  # Conversion automatique en int
    return {"message": f"Le numero du client à obtenir est: {user_id}"}

@app.post("/users/")
async def create_users(users: Users):  # Le modèle Pydantic devient le body
    return users.model_dump_json()

@app.get("/items/validated/{user_id}")
async def read_validated_item(
    user_id: int = Path(..., title="ID de l'article", gt=0, le=1000),
    q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^[a-z]+$"),
    size: float = Query(1.0, gt=0, lt=10.5)
):
    return {"item_id": user_id, "q": q, "size": size}