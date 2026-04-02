# Task Manager API

Simple backend API built with FastAPI.

## Features

- Get all tasks
- Create task
- Update task
- Delete task

## Tech Stack

- Python
- FastAPI
- Uvicorn

## Installation

```bash
git clone https://github.com/your-username/task-manager-api.git
cd task-manager-api
pip install -r requirements.txt


## Example API Usage

### Get all tasks
GET /tasks

### Create task
POST /tasks
{
  "title": "Learn Backend",
  "completed": false
}

### Update task
PUT /tasks/1
{
  "title": "Updated task",
  "completed": true
}

### Delete task
DELETE /tasks/1


## Project Status

This project was created as part of my backend learning journey.

Future improvements:
- Database integration
- Authentication
- Docker support
- Unit tests