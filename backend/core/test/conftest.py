import os
import sys
import pytest
from typing import Any,Generator
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.base_class import Base
from routers.base_router import api_router
from db.session import get_db


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 

def start_application():
    router=FastAPI()
    router.include_router(api_router)
    return router


SQALCHEMY_DATABASE_URL="sqlite:///./test_db.db"

engine=create_engine(SQALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False})

sessiontesting=sessionmaker(autocommit=False, autoflush=False,bind=engine)


pytest.fixture(scope="function")
def app()->Generator[FastAPI, Any, None]:
    Base.metadata.create_all(engine)
    app=start_application()
    yield app
    Base.metadata.drop_all(engine)

pytest.fixture(scope="function")
def db_session(app:FastAPI)-> Generator[sessiontesting, Any, None]:
    