from pydantic import BaseModel

class Comment_input(BaseModel):
    id:int
    text:str
    user_id:int
    post_id:int

class Show_comment(BaseModel):
    text:str
    class config:
        orm_mode=True