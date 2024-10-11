from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.orm import relationship

from app.models import Base

class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer(), primary_key=True, index=True)
    email = Column("email", String(100), unique=True)
    name = Column("name", String(100))
    password = Column("hashed_password", String(255))
    updated_at = Column("updated_at", DateTime(), default=current_timestamp())
    created_at = Column("created_at", DateTime(), default=current_timestamp())