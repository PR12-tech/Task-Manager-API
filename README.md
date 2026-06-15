# Task Manager API

A simple Task Manager REST API built using FastAPI.

## Features

* Create Tasks
* Read All Tasks
* Read Task By ID
* Update Tasks
* Delete Tasks
* Filter Tasks By Priority

## Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn
* Git
* GitHub

## API Endpoints

### GET

* `/tasks`
* `/tasks/{task_id}`

### POST

* `/tasks`

### PUT

* `/tasks/{task_id}`

### DELETE

* `/tasks/{task_id}`

### Query Parameters

* `/filter?priority=High`

## Run Locally

```bash
uvicorn main:app --reload
```

## API Documentation

Visit:

http://127.0.0.1:8000/docs
