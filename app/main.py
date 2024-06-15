from fastapi import FastAPI
from api.routes.todo import todo_router
from tortoise.contrib.fastapi import register_tortoise
import uvicorn 

app = FastAPI()
app.include_router(todo_router)

username = "postgres"
password = "root"
database_name = "postgres"


register_tortoise(
    app=app,
    db_url=f'postgres://{username}:{password}@localhost:5432/{database_name}',
    modules={'models': ['api.models.todo']},
    generate_schemas=True,
    add_exception_handlers=True,
)

app.get("/")
async def index (): 
    return {"status": "todo app is running"}

