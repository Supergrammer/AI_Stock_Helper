import json

from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_env = "local_db_config"
with open("app/config.json", 'r') as f:
    config = json.load(f)[db_env]
    
# {db}://{username}:{password}@{host}:{port}/{db_name}
SQLALCHEMY_DATABASE_URL = "{0}://{1}:{2}@{3}:{4}/{5}"\
    .format(config["db"], config["username"], config["password"], config["host"], config["port"], config["db_name"])

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try: return db
    finally: db.close()