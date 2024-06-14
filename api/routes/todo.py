from fastapi import APIRouter

todo_router = APIRouter(
    prefix = "/api", tags=  ["todo"]
)

@todo_router.get("/")
async def all_todo(): 
    return "Not implrmented"

@todo_router.post("/")
async def post_todo (): 
    return "Not implemented"

@todo_router.put("/{key}")
async def update_todo(key: int): 
    return "Not implemented"

@todo_router.delete("/{key}")
async def delete_todo(key:int): 
    return "Not implemented"