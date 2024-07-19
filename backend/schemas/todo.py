from typing import List, Optional

from models.Mtodo import TaskItem, todo

def todoEntity(item) -> Optional[todo]:
    if item:
        return todo(
            id=str(item["_id"]),
            name=item["name"],
            desc=item["desc"],
            date=item["date"],
            task=[TaskItem(**task) for task in item.get("task", [])]
        )
    return None

def todosEntity(entity) -> List[dict]:
    return [todoEntity(item) for item in entity]


