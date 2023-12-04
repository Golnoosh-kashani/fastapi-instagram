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
from db.models.users import User
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
    connection=engine.connect()
    transaction=connection.begin()
    session=sessiontesting(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


pytest.fixture(scope="function")
def create_test_user(db_session:sessiontesting):
    new_user=User(username="Testuser",email="Test@example.com",password="testt")
    db_session.add(new_user)
    db_session.commit()
    yield new_user.id
    # Optional teardown: delete the user after the test
    db_session.delete(new_user)
    db_session.commit()






pytest.fixture(scope="function")
def client(app:FastAPI,db_session:sessiontesting)->Generator[TestClient,Any,None]:
    def get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db]=get_test_db     
    with TestClient(app) as client:
        yield client   

