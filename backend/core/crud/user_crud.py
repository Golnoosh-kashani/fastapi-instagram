from db.session import get_db
from schemas.users import user_input
from sqlalchemy.orm import Session
from fastapi import Depends
from core.hashing import hasher
from schemas.users import user_input
from db.models.users import User

def create_new_user(db:Session,new_user:user_input):
    new_user=User(username=new_user.username,email=new_user.email,hashed_password=hasher.get_password_hash(new_user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
