from sqlalchemy import Column,Integer,String,Date,ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base


class User(Base):
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True,nullable=False,index=True)
    email=Column(String,unique=True,nullable=False)
    password=Column(String,nullable=False)
    posts=relationship("Post",back_populates="owner")