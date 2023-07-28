from app.db import dump_database, restore_database
from fastapi import APIRouter

router = APIRouter(prefix="/api/db")


# @router.get("/backup",
#             tags=['db'],
#             description='Сохранить базу данных')
# async def backup():
#     dump_database()


@router.get("/restore",
            tags=['db'],
            description='Восстановить базу данных')
async def restore():
    restore_database()
