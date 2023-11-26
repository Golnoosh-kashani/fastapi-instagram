from pydantic import BaseModel
from datetime import datetime,date
from typing import Text,Optional

class posts_input(BaseModel):
    id:int
    caption:Text
    image_path:str
    date_created:date
    owner_id:int

class show_post(BaseModel):
    caption:Text
    image_path:str
    date_created:date
    class config:
        orm_mode=True