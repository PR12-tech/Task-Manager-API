from fastapi import APIRouter
from schemas.task import Task
from sqlalchemy.orm import Session
from fastapi import Depends
from database import get_db
from models import TaskModel

router = APIRouter()


@router.get("/tasks")
def get_db_tasks(db: Session = Depends(get_db)):

    tasks = db.query(TaskModel).all()

    return tasks


@router.get("/tasks/{task_id}")
def get_tasks(
        task_id: int,
        db: Session = Depends(get_db)
):

        task = db.query(TaskModel).filter( #looks inside task table
            TaskModel.id == task_id
        ).first()                      #give me first matching row

        if task:
            return task

        return {
           "message": "Task Not Found"
        }


@router.post("/tasks")
def create_db_task(
        task: Task,
        db: Session = Depends(get_db)):

    new_task = TaskModel(
        task = task.task,
        priority = task.priority
    )

    db.add(new_task)

    db.commit()

    db.refresh(new_task)

    return {
        "message": "Task Added to database",
        "task": new_task
    }


@router.put("/tasks/{task_id}")
def update_task(
        task_id: int,
        update_task: Task,
        db: Session = Depends(get_db)
):

        task = db.query(TaskModel).filter(
            TaskModel.id == task_id
        ).first()

        if not task:
            return {
                "message": "Task Not Found"
            }

        task.task = update_task.task
        task.priority = update_task.priority

        db.commit()

        db.refresh(task)

        return {
            "message": "Task Updated",
            "task": task
        }


@router.delete("/tasks{task_id}")
def delete_task(
        task_id: int,
        db: Session = Depends(get_db)
):
    task = db.query(TaskModel).filter(
        TaskModel.id == task_id
    ).first()

    if not task:
        return {
            "message": "Task Not Found"
            }
    db.delete(task)

    db.commit()

    return {
        "message": "Task Deleted"
    }


@router.get("/filter")
def filter_tasks(
        priority: str,
        db: Session = Depends(get_db)
):

    tasks = db.query(TaskModel).filter(
        TaskModel.priority == priority
    ).all()

    return tasks
