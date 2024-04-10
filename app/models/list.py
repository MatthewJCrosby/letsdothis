from pydantic import BaseModel
from typing import List, Optional
from task import Task

class ListBase(BaseModel):
    #ListBase contains common attributes for a list.
    title: str
    description: Optional[str] = None

class CreateList(ListBase):
    #ListCreate is used for creating new lists.
    pass

class List_object(ListBase):
    #List is the main model for a list, including a list of tasks.
    id: int
    owner_id: int
    tasks: List['Task'] = []

    class Config:
        orm_mode = True