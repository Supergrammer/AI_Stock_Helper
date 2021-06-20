from sqlalchemy import Column, Integer, String, ARRAY
from sqlalchemy.orm import backref, relationship

from sqlalchemy.dialects.postgresql import UUID

import uuid

from .base_model import Base, BaseMixin

class User(Base, BaseMixin):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    email = Column(String(51), unique=True, index=True, nullable=False)
    password = relationship( \
        "Password",
        backref=backref("user", uselist=False),
        primaryjoin='foreign(User.id) == remote(Password.id)')
    
    username = Column(String(21), nullable=False)
    nickname = Column(String(51), nullable=True)
    authority = Column(ARRAY(String), nullable=True)