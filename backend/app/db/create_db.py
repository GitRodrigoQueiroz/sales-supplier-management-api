import os

from sqlalchemy.engine import create_engine

from backend.app.models import Base

try:
    from dotenv import find_dotenv, load_dotenv

    load_dotenv(find_dotenv())

except ModuleNotFoundError:
    pass


def create_postgresql_engine(
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

engine = create_postgresql_engine(**credentials_db)
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine, checkfirst=True)
