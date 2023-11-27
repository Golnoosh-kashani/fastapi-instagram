from pathlib import Path
import os
from dotenv import load_dotenv

env_path=Path('.')/'.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PEROJECT_TITLE:str="instagram-clone"
    PEROJECT_VERSION:str="0.1.1"
    POSTGRES_USER=os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER=os.getenv("POSTGRES_SERVER",default="localhost")
    POSTGRES_PORT=os.getenv("POSTGRES_PORT",default="5432")
    POSTGRES_DB=os.getenv("POSTGRES_DB",default="db_instagram") 
    POSTGRES_DATABASE_URL=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SECRET_KEY:str=os.getenv("SECRET_KEY")
    ALGORITHM="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    


settings=Settings()