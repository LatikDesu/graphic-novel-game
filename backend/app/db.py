import databases

from app.config import USER_DB, NAME_DB, PASSWORD_DB

DATABASE_URL = f"postgresql://{USER_DB}:{PASSWORD_DB}@db/{NAME_DB}"
database = databases.Database(DATABASE_URL)
