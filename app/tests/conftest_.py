import subprocess
import time

import pytest
from fastapi.testclient import TestClient

from app import app
from app.models import Base
from app.scripts.seed_db import insert_data_from_csv
from app.services.db_service import create_db_engine
from app.session import DATABASE_CREDENTIALS


@pytest.fixture(scope="function")
def client():
    engine = create_db_engine(**DATABASE_CREDENTIALS)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    insert_data_from_csv(engine)

    with TestClient(app) as client:
        yield client
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    subprocess.run(["docker-compose", "-f", "docker-compose.yml", "up", "-d"])
    time.sleep(10)
    yield

    subprocess.run(["docker-compose", "-f", "docker-compose.yml", "down"])
