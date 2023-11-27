from datetime import datetime,timedelta
from jose import jwt
from core.config import settings
from typing import Optional

def create_access_token(user_data:dict,expire_delta:timedelta):
    to_encode=user_data.copy()
    expire=datetime.utcnow()+expire_delta
    SECRET_KEY=settings.SECRET_KEY
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=settings.ALGORITHM)
    return encoded_jwt
