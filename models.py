from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

class Base(DeclarativeBase):
    pass

#IT is a SQLAlchemy Model Not a Pydantic Model which represents tasks table.
class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key = True, index = True)
    task = Column(String)
    priority = Column(String)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    user = relationship(
        "UserModel",
        back_populates = "tasks"
    )

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index = True)
    username = Column(String, unique = True, index = True)
    password = Column(String)

    tasks = relationship(
        "TaskModel",
        back_populates = "user"
    )