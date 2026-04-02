from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tasks = [
    {"id": 1, "title": "Learn FastAPI", "completed": False},
    {"id": 2, "title": "Build first backend", "completed": False}
]


@app.get("/")
def read_root():
    return {"message": "Hello from Denisa's backend"}


@app.get("/tasks")
def get_tasks():
    return tasks


class Task(BaseModel):
    title: str
    completed: bool = False


@app.post("/tasks")
def create_task(task: Task):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "completed": task.completed
    }
    tasks.append(new_task)
    return new_task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": f"Task {task_id} deleted successfully"}

    return {"error": "Task not found"}


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_task.title
            task["completed"] = updated_task.completed
            return task

    return {"error": "Task not found"}