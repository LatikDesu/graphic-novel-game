from typing import Optional

from pydantic import BaseModel, Field


class WindowModel(BaseModel):
    """Модель окна"""
    window_id: int
    character: str
    text: str
    path_img: str
    position: str

    class Config:
        orm_mode = True


class SceneModel(BaseModel):
    """Модель сцены"""
    scene_id: int
    name: str
    path_img: str
    windows: Optional[list[WindowModel]]

    class Config:
        orm_mode = True


class DialogRequest(BaseModel):
    """Схема запроса, для endpoint диалога"""
    start: int = Field(ge=0, default=0)
    end: int = Field(ge=0, default=0)


class SceneCreateModel(BaseModel):
    """Схема запроса, для endpoint создания сцены"""
    scene_id: int
    name: str
    path_img: str


class WindowCreateModel(BaseModel):
    """Схема запроса, для endpoint создания окна"""
    scene_id: int
    window_id: int
    character: str
    text: str
    path_img: str
    position: str


class WindowResponse(BaseModel):
    """Модель ответа на запрос окна"""
    scene_id: int
    window_id: int
    text: str
    character: str
    path_img: str
    position: str


class SceneResponse(BaseModel):
    """Модель ответа на запрос сцены"""
    scene: list[SceneModel]


class DialogResponse(BaseModel):
    """Модель ответа на запрос диалога"""
    dialogues: list[SceneResponse]
