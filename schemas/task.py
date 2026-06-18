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


class UserCreate(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class UserResponse(BaseModel):
    id: int
    username: str

    class config:
        from_attributes = True