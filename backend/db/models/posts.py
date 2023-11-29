from sqlalchemy import Column,String,Integer,Date,ForeignKey,Text
from sqlalchemy.orm import relationship
from db.base_class import Base
from db.models.comments import Comment
class Post(Base):
    id=Column(Integer,primary_key=True,index=True)
    caption=Column(Text)
    image_path=Column(String)
    date_created=Column(Date)
    owner_id=Column(Integer,ForeignKey('user.id'))
    owner=relationship("User",back_populates="posts")
    comments=relationship("Comment",back_populates="post")
