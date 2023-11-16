from fastapi import FastAPI
from core.config import settings



def start_application():
    app=FastAPI(title=settings.PEROJECT_TITLE,version=settings.PEROJECT_VERSION)
    return app

app=start_application()

@app.get("/")
def hello_api():
    return{"details":"hello api"}