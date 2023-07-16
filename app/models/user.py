from sqlalchemy import Boolean, Column, Integer, String, TIMESTAMP, text

from ..core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String, index=True)
    hashed_password = Column(String)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
