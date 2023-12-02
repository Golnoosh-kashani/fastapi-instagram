from fastapi import APIRouter, Depends,HTTPException,status
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from jose import jwt,JWTError
from db.session import get_db
from core.config import settings
from sqlalchemy.orm import Session
from db.models.users import User
from core.crud.user_crud import login_user
router=APIRouter()

@router.post("/login")
def user_login(db:Session=Depends(get_db),form_data:OAuth2PasswordRequestForm=Depends()):
    login_token=login_user(db=db,form_data=form_data)
    
    if not login_token:
        return{"an error happen"}
    else:
        return {"login has been successful"}
        


# get current user from token

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/login")
def get_current_user(db:Session=Depends(get_db),token:str=Depends(oauth2_scheme)):
    print(f"Received token: {token}")
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    parts = token.split('.')
    if len(parts) != 3:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token format")
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError as e:
         print(f"JWT Error: {e}")
         raise credentials_exception

    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise credentials_exception
    return user
   
