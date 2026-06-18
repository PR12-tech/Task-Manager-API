# Task Manager API

A RESTful Task Manager API built with FastAPI, SQLite, SQLAlchemy, and JWT Authentication.

## Features

* User Registration
* User Login
* JWT Authentication
* Protected Routes
* Create Tasks
* Get All Tasks
* Get Task By ID
* Update Tasks
* Delete Tasks
* Filter Tasks By Priority
* Swagger API Documentation
* SQLite Database Integration
* SQLAlchemy ORM

---

## Tech Stack

* FastAPI
* SQLite
* SQLAlchemy
* Pydantic
* JWT (python-jose)
* Passlib + bcrypt
* Uvicorn

---

## Project Structure

```text
Task_Manager_Api/
│
├── routers/
│   └── tasks.py
│
├── schemas/
│   └── task.py
│
├── auth.py
├── database.py
├── models.py
├── main.py
├── .gitignore
├── README.md
└── tasks.db
```

---

## Database Models

### User

| Field    | Type            |
| -------- | --------------- |
| id       | Integer         |
| username | String          |
| password | String (Hashed) |

### Task

| Field    | Type    |
| -------- | ------- |
| id       | Integer |
| task     | String  |
| priority | String  |

---

## API Endpoints

### Authentication

| Method | Endpoint  | Description                 |
| ------ | --------- | --------------------------- |
| POST   | /register | Register a new user         |
| POST   | /login    | Login and receive JWT token |

### Tasks

| Method | Endpoint         | Description             |
| ------ | ---------------- | ----------------------- |
| GET    | /tasks           | Get all tasks           |
| GET    | /tasks/{task_id} | Get task by ID          |
| POST   | /tasks           | Create task (Protected) |
| PUT    | /tasks/{task_id} | Update task             |
| DELETE | /tasks/{task_id} | Delete task             |

### Filtering

| Method | Endpoint               |
| ------ | ---------------------- |
| GET    | /tasks?priority=High   |
| GET    | /tasks?priority=Medium |
| GET    | /tasks?priority=Low    |

---

## Authentication Flow

1. Register a user using `/register`
2. Login using `/login`
3. Receive JWT Access Token
4. Click **Authorize** in Swagger UI
5. Paste the JWT token
6. Access protected endpoints

---

## Running the Project

### Clone Repository

```bash
git clone <repository-url>
cd Task_Manager_Api
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Server

```bash
uvicorn main:app --reload
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## Concepts Implemented

* REST API Development
* CRUD Operations
* SQLAlchemy ORM
* Dependency Injection
* Pydantic Validation
* Response Models
* HTTP Status Codes
* Exception Handling
* JWT Authentication
* Password Hashing
* Protected Routes
* Query Parameters
* SQLite Database Integration

---

## Future Improvements

* User-specific Tasks
* Task Ownership
* Database Relationships
* Refresh Tokens
* Role-Based Authorization
* Pagination
* Search and Sorting
* Docker Deployment
* PostgreSQL Integration
