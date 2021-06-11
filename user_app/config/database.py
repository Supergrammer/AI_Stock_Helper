from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker

from .config import get_configurations

c = get_configurations()

# {db}://{username}:{password}@{host}:{port}/{db_name}
SQLALCHEMY_DATABASE_URL = \
    "{0}://{1}:{2}@{3}:{4}/{5}" \
        .format(c.db, c.db_username, c.db_password, c.db_host, c.db_port, c.db_name)

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try: return db
    finally: db.close()