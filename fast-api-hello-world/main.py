#Python
from typing import Optional
from enum import Enum

#Pydantic
from pydantic import BaseModel
from pydantic import Field

#FastAPI
from fastapi import FastAPI
from fastapi import Body
from fastapi import Query, Path
app = FastAPI()

#Models
class HairColor(Enum):
    white = "white"
    browm = "browm"
    black = "black"
    blonde = "blonde"
    red = "red"

class Person(BaseModel):
    first_name: str = Field(...,min_length=1, max_length=50)
    last_name: str = Field(...,min_length=1, max_length=50)
    age: int = Field(..., gt=0, le=115)
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)

class Location(BaseModel):
    city: str
    state: str
    country: str


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

#Validaciones Query Parameters
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=50,
        title="Person Name",
        description="This is the person name, 1 and 50 chart"
        ),
    age : str = Query(
        ...,
        title="Person Age",
        description="This is the person age. It's required"
        )
):
    return {name: age}


#ge - greater or equal than >= (Mayor igual que)
#le - less or equal than <= (Menor igual que)
#gt - greater than > (Mayor)
#lt - less than < (Menor)

@app.get("/person/detail/{person_id}")
def show_person(person_id: int = Path(
    ...,
    gt=0,
    title="Person Id",
    description="This is Person Id"
    )):
    return {person_id: "It exists!"}


#Validaciones: Request Body
@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person Id",
        description="This is the Person Id",
        gt=0
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    return results



#Tipos Especiales
#Enum
#HttpUrl
#FilePath
#DirectoryPath
#EmailStr
#PaymentCardNumber
#IpvAnyAddress
#NegativeFloat
#PositiveFloat
#NegativeInt
#PositiveInt
