from app.db import database
from app.generator import Generator
from app.models.models import scene_table
from app.models.schemas import SceneCreateModel, SceneResponse
from fastapi import APIRouter
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/api/scene")


@router.get("/",
            tags=['scene'],
            description='Получить сцену', response_model=SceneResponse)
async def get_scene(scene_id: int):
    generator = Generator(request=scene_id)
    scene = await generator.generate_scene()
    return scene


@router.post("/create",
             tags=['scene'],
             description='Создать сцену')
async def create_scene(scene_request: SceneCreateModel):
    query = scene_table.select().where(scene_table.c.scene_id == scene_request.scene_id)
    test = await database.fetch_one(query)

    if test:
        return {"message": "Сцена уже существует"}

    query = scene_table.insert().values(scene_request.dict())

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
            tags=['scene'],
            description='Обновить сцену')
async def update_scene(scene_id: int, scene_request: SceneCreateModel):
    query = scene_table.select().where(scene_table.c.scene_id == scene_id)
    test = await database.fetch_one(query)

    if not test:
        return {"message": "Сцена не существует"}

    query = scene_table.update().where(scene_table.c.scene_id == scene_id). \
        values(scene_id=scene_request.scene_id,
               name=scene_request.name,
               path_img=scene_request.path_img)
    try:
        await database.execute(query)
        return {"message": "Сцена обновлена"}
    except:
        return {"message": "Сцена c таким scene_id занята, сначала измените ее"}


@router.delete("/delete",
               tags=['scene'],
               description='Удалить сцену')
async def delete_scene(scene_id: int):
    query = scene_table.delete().where(scene_table.c.scene_id == scene_id)

    try:
        await database.execute(query)
        return {"message": "Сцена удалена"}
    except:
        return {"message": "Сцена не существует"}
