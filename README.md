# Task Manager API

Simple backend REST API built with FastAPI implementing CRUD operations for task management.

## Features

- Get all tasks
- Create task
- Update task
- Delete task

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic

## Project Structure

task-manager-api/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

## Installation

Clone the repository:

git clone https://github.com/DenisaGotia/task-manager-api.git
cd task-manager-api

Create virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

## Run the Application

uvicorn main:app --reload

Application will run on:

http://127.0.0.1:8000

## API Documentation

FastAPI provides automatic interactive documentation:

http://127.0.0.1:8000/docs

## Example API Usage

### Get all tasks

GET /tasks

### Create task

POST /tasks

Request body:

{
  "title": "Learn Backend",
  "completed": false
}

### Update task

PUT /tasks/1

Request body:

{
  "title": "Updated task",
  "completed": true
}

### Delete task

DELETE /tasks/1

## CRUD Operations

This API supports full CRUD operations:

- Create → POST /tasks
- Read → GET /tasks
- Update → PUT /tasks/{id}
- Delete → DELETE /tasks/{id}

## Project Status

This project was created as part of my backend learning journey.

Future improvements:

- Database integration (PostgreSQL / SQLite)
- Authentication (JWT)
- Docker support
- Unit tests
- Better project structure
- Logging

## Learning Goals

This project demonstrates:

- REST API fundamentals
- CRUD operations
- FastAPI usage
- Request validation using Pydantic
- Backend project structure

## Author

Denisa Saracin

GitHub: https://github.com/DenisaGotia