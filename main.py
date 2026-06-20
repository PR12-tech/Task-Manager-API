from fastapi import FastAPI
from routers.tasks import router
from database import engine
from models import Base


app = FastAPI(
    title="Task Manager API",
    description="A RESTful Task Management API built with FastAPI, PostgreSQL, SQLAlchemy and JWT Authentication.",
    version="1.0.0"
)


app.include_router(router)


@app.get("/", tags = ["Home"])
def home():
    return {
        "message": "Welcome to Task Manager API"
    }


