# Task API

this is a simple CRUD app for tasks built using FastAPI, MongoDB and the Beanie ODM. 

## Run the application
1. Install all the dependencies for the project with
```
pip install -r requirements.txt
```
2. Run the application with
```
python run.py
```

## endpoints

- GET /tasks getalltasks
- POST /tasks createTask
- GET /tasks/{task_id} retrieveTask
- PUT /tasks/{task_id} updateTask
- DELETE /tasks/{task_id} deleteTask
