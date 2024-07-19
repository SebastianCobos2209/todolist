import datetime
from pydantic import BaseModel
from typing import Optional, List

class TaskItem(BaseModel):
    idtask: Optional[str]
    description: str
    completed: bool
    date: datetime.datetime

class todo(BaseModel):
    id: Optional[str]
    name: str
    desc: str
    date: datetime.datetime
    task: List[TaskItem]

