#Python
from typing import Optional,List

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body
app = FastAPI()

#Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


@app.get("/") #path operation decorator
def home(): #path operation function
    return {"Hello": "World"} #JSON

#path parameters
@app.get("/tweets/{id}")
def tweet(id):
    return {"params": id}

#Query Parameters
#Parameters Separator &
#/users/{user_id}/details?age=20&height=177
@app.get("/users/{user_id}/details")
def usersId(users_id):
    return {"id": users_id}

#Request Body y Response Body
@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person