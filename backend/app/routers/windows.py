from app.db import database
from app.models.models import window_table
from app.models.schemas import WindowCreateModel, WindowResponse
from fastapi import APIRouter
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/api/window")


@router.get("/",
            tags=['window'],
            description='Получить экран',
            response_model=WindowResponse)
async def get_window(scene_id: int, window_id: int):
    query = window_table.select().where(window_table.c.scene_id == scene_id).where(
        window_table.c.window_id == window_id)
    answer = await database.fetch_one(query)
    if answer:
        return WindowResponse(**dict(answer))
    return {"message": "Экран не найден"}


@router.post("/create",
             tags=['window'],
             description='Создать экран')
async def create_window(window_request: WindowCreateModel):
    query = window_table.select().where(window_table.c.scene_id == window_request.scene_id).where(
        window_table.c.window_id == window_request.window_id)
    test = await database.fetch_one(query)

    if test:
        return {"message": "Экран уже существует"}

    query = window_table.insert().values(window_request.dict())

    # TODO Заменить на триггеры
    success = False
    while not success:
        try:
            await database.execute(query)
            success = True
        except IntegrityError:
            database.rollback()

    return {"Сцена создана": "ОК"}


@router.put("/update",
            tags=['window'],
            description='Обновить экран')
async def update_scene(scene_id: int, window_id: int, window_request: WindowCreateModel):
    query = window_table.update().where(window_table.c.scene_id == scene_id).where(
        window_table.c.window_id == window_id).values(window_request.dict())
    try:
        await database.execute(query)
        return {"message": "Экран обновлен"}
    except:
        return {"message": "Экрана не существует"}


@router.delete("/delete",
               tags=['window'],
               description='Удалить экран')
async def delete_window(scene_id: int, window_id: int):
    query = window_table.delete().where(window_table.c.scene_id == scene_id).where(
        window_table.c.window_id == window_id)
    try:
        await database.execute(query)
        return {"message": "Экран удален"}
    except:
        return {"message": "Экрана не существует"}
