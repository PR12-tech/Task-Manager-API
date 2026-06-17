from fastapi import APIRouter
from schemas.task import TaskResponse, MessageResponse, TaskCreate, TaskUpdate
from sqlalchemy.orm import Session # ORM (Object Relational Mapper) converts Python objects into SQL Queries.
from fastapi import Depends
from database import get_db
from models import TaskModel
from fastapi import HTTPException
from fastapi import status

router = APIRouter()


@router.get(
    "/tasks",
    response_model=list[TaskResponse]
)

def get_db_tasks(
        priority: str | None = None,
        db: Session = Depends(get_db)
):

    if priority:

        return db.query(TaskModel).filter(
            TaskModel.priority == priority
        ).all()

    return db.query(TaskModel).all()


@router.get(
    "/tasks/{task_id}",
     response_model=TaskResponse,
     responses = {
         404: {"description": "Task Not Found"}
     }
)

def get_tasks(
        task_id: int,
        db: Session = Depends(get_db)
):

        task = db.query(TaskModel).filter(#looks inside task table
            TaskModel.id == task_id
        ).first()                        #give me first matching row

        if task:
            return task

        raise HTTPException(
            status_code = 404,
            detail = "Task Not Found"
        )


@router.post(
    "/tasks",
    response_model = TaskResponse,
    status_code = status.HTTP_201_CREATED
)

def create_db_task(
        task: TaskCreate,
        db: Session = Depends(get_db)):

    new_task = TaskModel(
        task = task.task,
        priority = task.priority
    )

    db.add(new_task)

    db.commit() #Used to save cahnges permanently.

    db.refresh(new_task)

    return new_task


@router.put(
    "/tasks/{task_id}",
    response_model=TaskResponse,
    responses={
        404: {"description": "Task Not Found"}
    }

)

def update_task(
        task_id: int,
        update_task: TaskUpdate,
        db: Session = Depends(get_db)
):

        task = db.query(TaskModel).filter(
            TaskModel.id == task_id
        ).first()

        if not task:
            raise HTTPException (
                status_code = 404,
                detail = "Task Not Found"
            )

        task.task = update_task.task
        task.priority = update_task.priority

        db.commit()

        db.refresh(task)

        return task


@router.delete(
    "/tasks/{task_id}",
    response_model = MessageResponse,
    responses = {
        404: {"description": "Task Not Found" }
    }
)

def delete_task(
        task_id: int,
        db: Session = Depends(get_db)
):
    task = db.query(TaskModel).filter(
        TaskModel.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code = 404,
            detail = "Task Not Found"
        )

    db.delete(task)

    db.commit()

    return MessageResponse(
        message = "Task Deleted"
    )




