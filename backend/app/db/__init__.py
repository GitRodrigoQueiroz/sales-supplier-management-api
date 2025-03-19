import os

from sqlalchemy.engine import create_engine

try:
    from dotenv import find_dotenv, load_dotenv

    load_dotenv(find_dotenv())

except ModuleNotFoundError:
    pass


def create_db_engine(
    user: str,
    password: str,
    host: str,
    port: str,
    database: str,
):
    conn_str = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(url=conn_str, echo=False)

    return engine


credentials_db = {
    "user": os.getenv("USER"),
    "password": os.getenv("PASSWORD"),
    "host": os.getenv("HOST"),
    "port": os.getenv("PORT"),
    "database": os.getenv("DATABASE"),
}
