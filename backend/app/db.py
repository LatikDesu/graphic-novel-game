import os
import subprocess

import databases
from app.config import USER_DB, NAME_DB, PASSWORD_DB

DATABASE_URL = f"postgresql://{USER_DB}:{PASSWORD_DB}@db/{NAME_DB}"
database = databases.Database(DATABASE_URL)


def dump_database():
    os.environ['PGPASSWORD'] = 'postgres'
    subprocess.run(["pg_dump", "-h", "db", "-U", "postgres", "-W", "-F", "c", "-f", "database.sql", "game_db"])


def restore_database():
    os.environ['PGPASSWORD'] = 'postgres'
    subprocess.run(["pg_restore", "-h", "db", "-U", "postgres", "-W", "-d", "game_db", "database.sql"])
