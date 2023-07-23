from app.db import database
from app.models.models import scene_table, window_table
from app.models.schemas import SceneModel
from app.models.schemas import SceneResponse, DialogResponse


class Generator:
    """
    Генератор ответов сцен и диалогов
    """

    def __init__(self, request) -> None:
        self.request = request

    async def generate_scene(self) -> SceneResponse:
        id = self.request

        query = scene_table.select().where(scene_table.c.scene_id == id)
        scene = await database.fetch_one(query)
        if scene:
            scene_model = SceneModel(**dict(scene))

            query = window_table.select().where(window_table.c.scene_id == id).order_by(window_table.c.window_id)
            windows = await database.fetch_all(query)
            windows_model = [dict(window) for window in windows]
            scene_model.windows = windows_model

            return SceneResponse(scene=[scene_model])
        else:
            return SceneResponse(scene=[])

    async def generate_dialog(self) -> DialogResponse:
        if self.request.start == 0 and self.request.end == 0:
            query = scene_table.select().order_by(scene_table.c.scene_id)
        else:
            query = scene_table.select().where(
                scene_table.c.scene_id.between(self.request.start - 1, self.request.end - 1)).order_by(
                scene_table.c.scene_id)

        scenes = await database.fetch_all(query)
        scenes_models = [await take_scene(scene) for scene in scenes]
        return DialogResponse(dialogues=scenes_models)


async def take_scene(scene) -> SceneResponse:
    scene_model = SceneModel(**dict(scene))
    query = window_table.select().where(window_table.c.scene_id == scene.scene_id).order_by(window_table.c.window_id)
    windows = await database.fetch_all(query)
    windows_model = [dict(window) for window in windows]
    scene_model.windows = windows_model

    return SceneResponse(scene=[scene_model])
