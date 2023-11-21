from fastapi import FastAPI,Depends,Form,File,UploadFile
from typing import Optional,Text
from core.config import settings
from core.crud.user_crud import create_new_user
from core.crud.post_crud import create_new_post
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.users import user_input
import os
import sys
print(sys.path)
def start_application():
    app=FastAPI(title=settings.PEROJECT_TITLE,version=settings.PEROJECT_VERSION)
    os.makedirs('images', exist_ok=True)

    return app


app=start_application()

@app.get("/")
def hello_api():
    
    return{"details":"hello api"}

@app.post("/")
def create_new_user(user:user_input,db:Session=Depends(get_db)):
    add_user=create_new_user(user,db)
    return add_user

@app.post("/post")
def Create_new_post_router(owner_id:int,db:Session=Depends(get_db),image:UploadFile = File(None), 
                          caption: Text = Form(...)):
    
    new_post=create_new_post(db,image,caption)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
