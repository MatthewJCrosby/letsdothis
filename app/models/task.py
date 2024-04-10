from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskBase(BaseModel):
    #TaskBase includes common attributes.
    title: str
    description: Optional[str] = None
    due_date: Optional[str] = None
    status: str
    urgency: Optional[str]= None

class CreateTask(TaskBase):
    #TaskCreate is used when creating a new task.
    pass

class Task(TaskBase):
    #Task is the detailed model for a task, including its relation to a list.
    id: int
    list_id: int

    class Config:
        orm_mode = True