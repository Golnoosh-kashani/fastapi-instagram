from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from core.config import settings
from typing import Generator
DATABASE_URL=settings.POSTGRES_DATABASE_URL
engine=create_engine(DATABASE_URL)
session=sessionmaker(autoflush=False,autocommit=False,bind=engine)

def get_db()->Generator:
    try:
        db=session
        yield db
    finally:
        db.close()   
