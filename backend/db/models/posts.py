from sqlalchemy import Column,String,Integer,Date,ForeignKey,text
from sqlalchemy.orm import relationship
from db.base_class import Base

class Posts(Base):
    id=Column(Integer,primary_key=True,index=True)
    caption=Column(text)
    image_path=Column(String)
    date_created=Column(Date)
    owner_id=Column(Integer,ForeignKey('user.id'))
