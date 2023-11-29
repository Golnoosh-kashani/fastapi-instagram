from fastapi import APIRouter, Depends,HTTPException,status
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from db.session import get_db
from sqlalchemy.orm import Session
from core.crud.user_crud import login_user
router=APIRouter()

@router.post("/login")
def user_login(db:Session=Depends(get_db),form_data:OAuth2PasswordRequestForm=Depends()):
    login_token=login_user(db=db,form_data=form_data)
    if not login_token:
        return{"an error happen"}
        


