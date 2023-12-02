from pydantic import BaseModel
from datetime import datetime,date
from typing import Text,Optional

class posts_input(BaseModel):
    id:int
    caption:Text
    image_path:str
    date_created:date
    owner_id:int
    #class config:
        #orm_mode=True

class show_post(posts_input):
     
     
     caption:Text
     image_path:str
     date_created:date
     owner_id:int
     class config:
        orm_mode=True