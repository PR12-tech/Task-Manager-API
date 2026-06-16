from fastapi import APIRouter
from data import tasks
from schemas.task import Task

router = APIRouter()

@router.get("/tasks")
def get_tasks():
    return tasks

@router.get("/tasks/{task_id}")
def  get_tasks(task_id: int):

    for task in tasks:

        if task["id"] == task_id:
            return task

    return {
        "message": "Task Not Found"
    }

@router.post("/tasks")
def create_task(task: Task):

    new_task = task.model_dump()

    new_task["id"] = len(tasks) + 1

    tasks.append(new_task)

    return {
        "message": "Task Added",
        "task": new_task
    }

@router.put("/tasks{task_id}")
def update_task(task_id: int, update_task: Task):

    for task in tasks:

        if task["id"] == task_id:

            task["task"] = update_task.task
            task["priority"] = update_task.priority

            return {
                "message": "Task Updated"
            }

    return {
        "message": "Task Not Found"
    }

@router.delete("/tasks{task_id}")
def delete_task(task_id: int):

    for task in tasks:

        if task["id"] == task_id:

            tasks.remove(task)

            return {
                "message": "Task Deleted"
            }

@router.get("/filter")
def filter_tasks(priority: str):

    filtered_tasks = []

    for task in tasks:

        if task["priority"] == priority:
            filtered_tasks.append(task)

        return filtered_tasks