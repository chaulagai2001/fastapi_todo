from fastapi import FastAPI
from api.routes.todo import todo_router
import uvicorn 

app = FastAPI()
app.include_router(todo_router)

app.get("/")
async def index (): 
    return {"status": "todo app is running"}

