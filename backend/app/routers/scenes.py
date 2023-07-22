from app.db import database
from app.generator import Generator
from app.models.models import scene_table
from app.models.schemas import SceneCreateModel, SceneResponse
from fastapi import APIRouter

router = APIRouter(prefix="/api/scene")


@router.get("/",
            tags=['scene'],
            description='Получить сцену', response_model=SceneResponse)
async def get_scene(id: int):
    generator = Generator(request=id)
    scene = await generator.generate_scene()
    return scene


@router.post("/create",
             tags=['scene'],
             description='Создать сцену')
async def create_scene(scene_request: SceneCreateModel):
    query = scene_table.insert().values(scene_request.dict())
    scene_id = await database.execute(query)
    return {"id": scene_id}


@router.put("/update",
            tags=['scene'],
            description='Обновить сцену')
async def update_scene(id: int, scene_request: SceneCreateModel):
    query = scene_table.update().where(scene_table.c.id == id).values(scene_request.dict())
    await database.execute(query)
    return {"message": "Сцена обновлена"}


@router.delete("/delete",
               tags=['scene'],
               description='Удалить сцену')
async def delete_scene(id: int):
    query = scene_table.delete().where(scene_table.c.id == id)
    await database.execute(query)
    return {"message": "Сцена удалена"}
