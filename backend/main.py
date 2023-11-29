from fastapi import FastAPI
from core.config import settings
from core.routers.user_routers import router as user_routers
from core.routers.post_routers import router as post_routers
from core.routers.login_router import router as login_router
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
    app.include_router(user_routers)
    app.include_router(post_routers)
    app.include_router(login_router)
    create_tables()
    os.makedirs('images', exist_ok=True)

    return app


app=start_application()

@app.get("/")
def hello_api():
    
    return{"details":"hello api"}








