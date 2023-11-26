from db. base_class import Base
from sqlalchemy import Integer,String,Column,ForeignKey
from sqlalchemy.orm import relationship

class Comment(Base):
    id=Column(Integer,primary_key=True,index=True)
    text=Column(String,index=True)
    user_id=Column(ForeignKey("user.id"))
    post_id=Column(ForeignKey("post.id"))
    user = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")