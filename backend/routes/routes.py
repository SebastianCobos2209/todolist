from fastapi import APIRouter, HTTPException
from config.db import conn
from schemas.todo import todoEntity,todosEntity
from models.Mtodo import TaskItem, todo
from bson import ObjectId

user=APIRouter()

@user.get('/todo',response_model=list[todo])
def all_todo():
    return todosEntity(conn.local.todo.find().limit(1000))

@user.post('/todo')
def add_todo(todo:todo):
    new_todo=dict(todo)
    new_todo['task'] = [task.dict() for task in new_todo['task']]
    id=conn.local.todo.insert_one(new_todo).inserted_id
    todos=conn.local.todo.find_one({"_id":id})
    return todoEntity(todos)

@user.post('/task/{id}')
def add_task(id: str, task: TaskItem):
    task_dict = task.model_dump()
    result = conn.local.todo.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$push": {"task": task_dict}},
            return_document=True
        )
    return todoEntity(result)

@user.get('/todo/{id}')
async def findtodo(id:str):
    return todoEntity(conn.local.todo.find_one({"_id":ObjectId(id)}))

@user.put('/todo/update/{id}')
def update_todo(id:str, todo:todo):
    update_dict = todo.model_dump(exclude_unset=True, exclude={"id"})
    conn.local.todo.find_one_and_update( {"_id": ObjectId(id)},
            {"$set": update_dict},)
    return 


@user.put('/task/update/{id}', response_model=todo)
async def update_task(id:str ,task_update: TaskItem):
    task_dict = task_update.model_dump(exclude_unset=True)
    result = conn.local.todo.find_one_and_update(
        {"_id": ObjectId(id), "task.description": task_dict.get("description")},
        {"$set": {"task.$": task_dict}},
        return_document=True
    )
    if result:
            return todoEntity(result)
    else:
            raise HTTPException(status_code=404, detail="Todo or Task not found")
    


@user.delete('/todo/delete/{id}')
def delete_todo(id:str):
    deleted_todo = conn.local.todo.find_one_and_delete({"_id": ObjectId(id)})
    return todoEntity(deleted_todo)

@user.delete('/task/delete/{id}',response_model=todo)
def delete_todo(id:str,task_update: TaskItem):
    task_dict = task_update.model_dump(exclude_unset=True)
    result = conn.local.todo.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$pull": {"task": {"description": task_dict["description"]}}},
            return_document=True
        )
    if result:
            return todoEntity(result)
    else:
            raise HTTPException(status_code=404, detail="Todo or Task not found")
