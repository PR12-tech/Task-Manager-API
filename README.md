# Task Manager API

A RESTful Task Management API built with FastAPI, PostgreSQL, SQLAlchemy, 
and JWT Authentication. This project allows users to securely manage their 
tasks with full CRUD functionality while ensuring that users can only access 
their own data.

## Live API Documentation

🔗 https://task-manager-api-x41v.onrender.com/docs

## Features

- User Registration
- User Authentication using JWT
- Secure Password Hashing
- Create Tasks
- Retrieve Tasks
- Update Tasks
- Delete Tasks
- User-specific Task Ownership
- PostgreSQL Database Integration
- Database Migrations with Alembic
- Cloud Deployment on Render

## Tech Stack

### Backend
- FastAPI
- Python

### Database
- PostgreSQL

### ORM
- SQLAlchemy

### Authentication
- JWT (JSON Web Tokens)
- Passlib (bcrypt)

### Database Migrations
- Alembic

### Deployment
- Render
- PostgreSQL(Render Managed Database)

---

## Project Structure

```text
Task_Manager_Api/
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   ├── README
│   └── script.py.mako
│
├── routers/
│   ├── __init__.py
│   └── tasks.py
│
├── schemas/
│   ├── __init__.py
│   └── task.py
│
├── .env
├── .gitignore
├── alembic.ini
├── auth.py
├── database.py
├── main.py
├── models.py
├── requirements.txt
└── README.md
```

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|----------|----------|----------|
| POST | `/register` | Register a new user |
| POST | `/login` | Login and receive JWT token |

### Tasks

| Method | Endpoint | Description |
|----------|----------|----------|
| POST | `/tasks` | Create a task |
| GET | `/tasks` | Retrieve all user tasks |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

---

## Installation

### Clone Repository

```bash
git clone https://github.com/PR12-tech/Task-Manager-API.git
cd Task_Manager_Api
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Apply Database Migrations

```bash
alembic upgrade head
```

### Run Application

```bash
uvicorn main:app --reload
```

---

## Example Workflow

1. Register a User
2. Login to Obtain JWT Token
3. Authorize Using Swagger UI
4. Create Tasks
5. View Tasks
6. Update Tasks
7. Delete Tasks

---

## Learning Outcomes

This project helped me gain practical experience with:

- FastAPI Development
- REST API Design
- JWT Authentication
- PostgreSQL Integration
- SQLAlchemy ORM
- Alembic Migrations
- Environment Variables
- Cloud Deployment using Render
- Production Debugging and Troubleshooting

---

## Future Improvements

- Task Categories
- Task Due Dates
- Task Search & Filtering
- Pagination
- Docker Support
- Automated Testing
- CI/CD Pipeline

---

## Author

**Prasad Kadam**

Backend Developer Project built to gain hands-on experience with FastAPI, 
PostgreSQL, JWT Authentication, database migrations using Alembic, and cloud deployment on Render.