from fastapi import FastAPI
from core.config import settings
from core.routers.base_router import api_router
from sqlalchemy.orm import Session
from db.base_class import Base
from db.session import engine
import os
import sys
print(sys.path)

def create_tables():
    Base.metadata.create_all(engine)



def start_application():
    app=FastAPI(title=settings.PEROJECT_TITLE,version=settings.PEROJECT_VERSION)
    app.include_router(api_router)
   
    create_tables()
    os.makedirs('images', exist_ok=True)

    return app


app=start_application()

@app.get("/")
def hello_api():
    
    return{"details":"hello api"}








