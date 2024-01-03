import os
import sys
import pytest
from typing import Any,Generator
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
from db.base_class import Base
from core.routers.base_router import api_router
from db.models.users import User
from db.models.posts import Post
from db.session import get_db

print("Before:", sys.path)
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
print("After:", sys.path)


def start_application():
    router=FastAPI()
    router.include_router(api_router)
    return router


SQALCHEMY_DATABASE_URL="sqlite:///./test_db.db"

engine=create_engine(SQALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False})

sessiontesting=sessionmaker(autocommit=False, autoflush=False,bind=engine)


@pytest.fixture(scope="function")
def app()->Generator[FastAPI, Any, None]:
    Base.metadata.create_all(engine)
    app=start_application()
    yield app
    Base.metadata.drop_all(engine)



@pytest.fixture(scope="function")
def db_session(app:FastAPI)-> Generator[sessiontesting, Any, None]:
    connection=engine.connect()
    transaction=connection.begin()
    session=sessiontesting(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def create_test_user(db_session:sessiontesting):
    new_user=User(username="testuser",email="Test@example.com",password="testpassword")
    db_session.add(new_user)
    db_session.commit()
    yield new_user
    # Optional teardown: delete the user after the test
    db_session.delete(new_user)
    db_session.commit()

@pytest.fixture(scope="function")
def log_in_test_user():
    client = TestClient(app)
    login_data = {
        "username": "testuser",  # Replace with your test user's username
        "password": "testpassword"  # Replace with your test user's password
    }
    response = client.post("/login", data=login_data)  # Replace "/login" with your login endpoint
    token = response.json()["access_token"]  # Adjust this according to your response structure
    return token







@pytest.fixture(scope="function")
def test_post_id(db_session:sessiontesting,create_test_user):
    try:
        test_post=Post(caption="Test Caption",image_path="test_image.jpg",owner_id=create_test_user)
        db_session.add(test_post)
        db_session.commit()
        db_session.refresh(test_post)
        yield test_post.id
    finally:
        # Optionally, delete the post after the test
        db_session.delete(test_post)
        db_session.commit()
        db_session.close()


    



@pytest.fixture(scope="function")
def client(app:FastAPI,db_session:sessiontesting)->Generator[TestClient,Any,None]:
    def get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db]=get_test_db     
    with TestClient(app) as client:
        yield client   

