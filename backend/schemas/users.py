from pydantic import BaseModel,EmailStr
from datetime import datetime,date

class user_input(BaseModel):
    #id:int
    username:str
    email:EmailStr
    password:str
    date_joined:date

class ShowUser(BaseModel):
    username:str
    email:EmailStr
    class config:
        orm_mode=True    


