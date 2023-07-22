from app.db import database
from app.models.models import window_table
from app.models.schemas import WindowCreateModel
from fastapi import APIRouter

router = APIRouter(prefix="/api/window")


@router.get("/",
            tags=['window'],
            description='Получить экран')
async def get_window(id: int):
    query = window_table.select().where(window_table.c.window_id == id)
    return await database.fetch_one(query)


@router.post("/create",
             tags=['window'],
             description='Создать экран')
async def create_window(window_request: WindowCreateModel):
    query = window_table.insert().values(window_request.dict())
    window_id = await database.execute(query)
    return {"id": window_id}


@router.put("/update",
            tags=['window'],
            description='Обновить экран')
async def update_scene(id: int, window_request: WindowCreateModel):
    query = window_table.update().where(window_table.c.window_id == id).values(window_request.dict())
    await database.execute(query)
    return {"message": "Экран обновлен"}


@router.delete("/delete",
               tags=['window'],
               description='Удалить экран')
async def delete_window(id: int):
    query = window_table.delete().where(window_table.c.window_id == id)
    await database.execute(query)
    return {"message": "Экран удален"}
