# Task Manager API

A REST API built using FastAPI, SQLAlchemy, and SQLite for managing tasks.


## Features

* Create Tasks
* View All Tasks
* View Task By ID
* Update Existing Tasks
* Delete Tasks
* Filter Tasks By Priority
* SQLite Database Integration
* SQLAlchemy ORM
* FastAPI Router-Based Project Structure
* Automatic API Documentation with Swagger UI


## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn


## Project Structure

Task_Manager_API/

├── routers/

│   └── tasks.py

├── schemas/

│   └── task.py

├── database.py

├── models.py

├── main.py

├── .gitignore

└── README.md


## API Endpoints

| Method | Endpoint                | Description              |
|--------|-------------------------|--------------------------|
| GET    | `/tasks`                | Get all tasks            |
| GET    | `/tasks/{task_id}`      | Get task by ID           |
| POST   | `/tasks`                | Create a task            |
| PUT    | `/tasks/{task_id}`      | Update a task            |
| DELETE | `/tasks/{task_id}`      | Delete a task            |
| GET    | `/filter?priority=High` | Filter tasks by priority |


## How To Run

1. Clone the repository

2. Create a virtual environment

3. Install dependencies

pip install fastapi uvicorn sqlalchemy

4. Start the server

uvicorn main:app --reload

5. Open Swagger Docs

http://127.0.0.1:8000/docs


## Future Improvements

* Authentication (JWT)
* MySQL/PostgreSQL Support
* User Management
* Deployment
* AI Features
