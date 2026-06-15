from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    task: str
    priority: str


tasks = [
    {
        "id": 1,
        "task": "Study DSA",
        "priority": "High"
    },
    {
        "id": 2,
        "task": "Learn FastAPI",
        "priority": "Medium"
    }
]


@app.get("/")
def home():
    return {
        "message": "Welcome to Task Manager API"
    }


@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}") #Path Prameter: Used to identify a specific Resource.
def get_tasks(task_id: int):

    for task in tasks:

        if task["id"] == task_id:
            return task

    return {
        "message": "Task not Found"
    }


@app.post("/tasks")
def create_task(task: Task):

    new_task = task.model_dump()

    new_task["id"] = len(tasks) + 1

    tasks.append(new_task)

    return {
        "message": "Task Added",
        "task": new_task
    }


@app.get("/filter")#Used to filter or search data
def filter_tasks(priority: str):

    filtered_tasks = []

    for task in tasks:

        if task["priority"] == priority:
            filtered_tasks.append(task)

    return filtered_tasks


@app.put("/tasks/{task_id}")#Path parameter finds which task to update using id.
def update_task(task_id: int, updated_task: Task):
    #Pydantic object (updated_task) contains WHAT new values to update it with.
    for task in tasks:

        if task["id"] == task_id:

            task["task"] = updated_task.task
            task["priority"] = updated_task.priority

            return {
                "message": "Task Updated"
            }

    return {
        "message": "Task not Found"
    }


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    for task in tasks:

        if task["id"] == task_id:

            tasks.remove(task)

            return {
                "message": "Task Deleted"
            }

    return {
        "message": "Task Not Found!"
    }