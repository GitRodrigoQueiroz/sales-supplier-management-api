from backend.app.db import create_db_engine, credentials_db
from backend.app.models import Base

engine = create_db_engine(**credentials_db)
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine, checkfirst=True)
