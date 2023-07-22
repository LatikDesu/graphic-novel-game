from app.generator import Generator
from app.models.schemas import DialogRequest, DialogResponse
from fastapi import APIRouter

router = APIRouter(prefix="/api/dialog")


@router.post("/",
             tags=['dialog'],
             description='Получить список диалогов',
             response_model=DialogResponse)
async def get_dialog(dialog_request: DialogRequest):
    generator = Generator(request=dialog_request)
    dialog = await generator.generate_dialog()
    return dialog
