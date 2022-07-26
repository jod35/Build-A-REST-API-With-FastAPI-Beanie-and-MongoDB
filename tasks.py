from fastapi import APIRouter, HTTPException
from models import Task
from typing import List
from beanie import PydanticObjectId
from bson import ObjectId

task_router = APIRouter()


@task_router.get("/", status_code=200)
async def getalltasks() -> List[Task]:
    tasks = await Task.find_all().to_list()

    return tasks


@task_router.post("/", status_code=201)
async def createTask(task: Task):
    await task.create()

    return {"message": "Task has been saved"}


@task_router.get("/{task_id}", status_code=200)
async def retrieveTask(task_id: PydanticObjectId) -> Task:
    print(task_id)
    task_to_get = await Task.get(task_id)

    print(task_to_get)

    return task_to_get


@task_router.put("/{task_id}", status_code=200)
async def updateTask(task: Task, task_id: PydanticObjectId) -> Task:

    task_to_update = await Task.get(task_id)

    if not task_to_update:
        raise HTTPException(status_code=404, detail="Resource not found")

    task_to_update.task_content = task.task_content
    task_to_update.is_complete = task.is_complete

    await task_to_update.save()

    return task_to_update


@task_router.delete("/{task_id}", status_code=204)
async def deleteTask(task_id: PydanticObjectId):
    task_to_delete = await Task.get(task_id)

    await task_to_delete.delete()

    return {"message": "Task deleted"}
