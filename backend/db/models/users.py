from sqlalchemy import Column,Integer,String,Date,ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base
from db.models.comments import Comment

class User(Base):
    id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    username=Column(String,unique=True,nullable=False,index=True)
    email=Column(String,unique=True,nullable=False)
    password=Column(String,nullable=False)
    posts=relationship("Post",back_populates="owner")
    comments=relationship("Comment",back_populates="user")