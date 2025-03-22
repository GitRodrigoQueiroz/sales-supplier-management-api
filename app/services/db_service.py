from typing import Iterator

from fastapi import Depends
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.session import DATABASE_CREDENTIALS


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


@Depends
def get_session() -> Iterator[Session]:
    engine = create_db_engine(**DATABASE_CREDENTIALS)
    SessionLocal = sessionmaker(bind=engine)
    with SessionLocal() as session:
        yield session
