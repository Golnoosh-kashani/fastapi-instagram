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

def delete_user_by_id(user_id,db:Session):
    user=db.query(User).filter(User.id==user_id).first()
    if user:
        # If user is found, delete the user
        db.delete(user)
        db.commit()
       # print(f"User with ID {user_id} has been deleted.")
   

def update_user_by_id(user_id:int ,db:Session,user_new_data:dict):
     #param user_new_data dictionery contain user information
     user=db.query(User).filter(User.id==user_id).first()
     if user:
          # Update user attributes
          for key,value in user_new_data.items():
               if hasattr(user,key):
                setattr(user,key,value)

          db.commit()
          print(f"User with ID {user_id} has been updated.")
     else:
          print(f"User with ID {user_id} not found.")
                 
          

def get_all_users(db:Session):
    users=db.query(User).all()
    return users
    
    
   

   