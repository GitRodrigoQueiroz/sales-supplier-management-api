from typing import Iterator

from sqlalchemy.orm import Session, sessionmaker

from backend.app.db import create_db_engine, credentials_db


def get_session() -> Iterator[Session]:
    engine = create_db_engine(**credentials_db)
    with sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    ) as session:
        yield session
