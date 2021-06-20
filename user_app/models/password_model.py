from sqlalchemy import Column, Integer, String, ARRAY
from sqlalchemy.dialects.postgresql import UUID

import uuid

from .base_model import Base, BaseMixin

class Password(Base, BaseMixin):
    __tablename__ = "password"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    password_history = Column(ARRAY(String(65)), nullable=False)