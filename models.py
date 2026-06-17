from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String

class Base(DeclarativeBase):
    pass

#IT is a SQLAlchemy Model Not a Pydantic Model which represents tasks table.
class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key = True, index = True)
    task = Column(String)
    priority = Column(String)