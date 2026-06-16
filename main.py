from fastapi import FastAPI
from schemas.task import Task
from data import tasks
from routers.tasks import router

app = FastAPI()

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Task Manager API"
    }
