from typing import Optional

from pydantic import BaseModel, Field


class WindowModel(BaseModel):
    """Модель окна"""
    window_id: int
    character: Optional[str] = None
    text: Optional[str] = None
    path_img: Optional[str] = None
    position: Optional[str] = None

    class Config:
        orm_mode = True


class SceneModel(BaseModel):
    """Модель сцены"""
    scene_id: int
    name: str
    path_img: str

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
    character: Optional[str] = None
    text: Optional[str] = None
    path_img: Optional[str] = None
    position: Optional[str] = None


class WindowResponse(BaseModel):
    """Модель ответа на запрос окна"""
    scene_id: int
    window_id: int
    text: Optional[str] = None
    character: Optional[str] = None
    path_img: Optional[str] = None
    position: Optional[str] = None


class SceneResponse(BaseModel):
    """Модель ответа на запрос сцены"""
    scene: list[SceneModel]
    windows: list[WindowResponse]


class DialogResponse(BaseModel):
    """Модель ответа на запрос диалога"""
    dialogues: list[SceneResponse]
