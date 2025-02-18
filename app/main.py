from fastapi import FastAPI
from app.tasks import create_task
from pymongo import MongoClient

client = MongoClient("mongodb://mongodb:27017/")
db = client["celery_db"]
collection = db["task_results"]

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI with Celery and Docker Compose"}

@app.get("/api/v1")
def read_root():
    return {"message": "FastAPI with Celery and Docker Compose API v1 and CI pipeline"}

@app.get("/api/v2")
def read_root():
    return {"message": "FastAPI with Celery and Docker Compose API v2 and CI pipeline"}

@app.get("/api/v2/tasks")
def read_root():
    return {"message": "FastAPI with Celery and Docker Compose API v2 tasks for CI pipeline"}

@app.post("/tasks/{data}")
def run_task(data: str):
    task = create_task.delay(data)
    return {"task_id": task.id, "status": "Processing"}

@app.get("/tasks/")
def get_all_tasks():
    tasks = list(collection.find({}, {"_id": 0}))
    return {"tasks": tasks}

