from backend.app.models import Base
from backend.app.session import create_db_engine, credentials_db

engine = create_db_engine(**credentials_db)
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine, checkfirst=True)
