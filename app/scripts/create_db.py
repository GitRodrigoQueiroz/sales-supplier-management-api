from backend.app.models import Base
from backend.app.services.db_service import create_db_engine
from backend.app.session import DATABASE_CREDENTIALS

engine = create_db_engine(**DATABASE_CREDENTIALS)
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine, checkfirst=True)
