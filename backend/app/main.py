from logging.config import dictConfig

import sqlalchemy
from app.db import DATABASE_URL, database
from app.logger import LogConfig
from app.routers import dialogues, windows, scenes, db
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

dictConfig(LogConfig().dict())

app = FastAPI(
    title="GAME API",
    description="The graphic novel API for the RSHB hackathon is a set of tools and interfaces that allow "
                "you to create and run interactive stories in graphic novel format. ",
    contact={"name": "РСХБ_хак_Команда 6",
             "url": "https://rshbdigital.ru/"},
    version="0.1.0",
    docs_url="/documentation",
    redoc_url=None,
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dialogues.router)
app.include_router(scenes.router)
app.include_router(windows.router)
app.include_router(db.router)
