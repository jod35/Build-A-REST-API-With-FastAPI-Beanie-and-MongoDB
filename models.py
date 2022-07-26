from datetime import datetime
from beanie import Document, PydanticObjectId
from pydantic import Field
from bson.objectid import ObjectId


class Task(Document):
    task_content: str = Field(max_length=400)
    is_complete: bool = False
    date_created: datetime = datetime.now()

    class Settings:
        name = "tasks_database"

    class Config:
        schema_extra = {
            "task_content": "A sample content",
            "is_complete": True,
            "date_created": datetime.now(),
        }
