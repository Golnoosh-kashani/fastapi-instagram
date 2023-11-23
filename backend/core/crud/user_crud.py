from db.session import get_db
from schemas.users import user_input
from sqlalchemy.orm import Session
from fastapi import Depends
from core.hashing import hasher
from schemas.users import user_input
from db.models.users import User

def create_new_user(user_data: user_input, db: Session ):
   
    #add user in database
    new_user = User(username=user_data.username, email=user_data.email, 
                    password=hasher.get_password_hash(user_data.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user