from fastapi import FastAPI
from routers.tasks import router
from database import engine
from models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Task Manager API"
    }
