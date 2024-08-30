from fastapi import FastAPI
from typing import List
from app.models.User import User

app =  FastAPI()

db : List[User] = []


@app.get("/")
def root():
    return {"Hello" : "world"} 

@app.post("/add/user")
async def add(user: User):
    db.append(user);
    return user;
        
