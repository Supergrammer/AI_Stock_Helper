from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker

from .config import get_configurations

c = get_configurations()

SQLALCHEMY_DATABASE_URL = \
    f"{c.db}://{c.db_username}:{c.db_password}@{c.db_host}:{c.db_port}/{c.db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try: return db
    finally: db.close()