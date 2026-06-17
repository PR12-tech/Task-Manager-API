from pydantic import BaseModel

#This is used for user input request validation.
class TaskCreate(BaseModel):
    task: str
    priority: str


class TaskUpdate(BaseModel):
    task: str
    priority: str


#This is Validation for Response that goes out of the API.
class TaskResponse(BaseModel):

    id: int
    task: str
    priority: str

    class Config:
        from_attributes = True


class MessageResponse(BaseModel):

    message: str