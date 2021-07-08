from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseMixin():
    created_date = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    updated_date = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now(), nullable=False)