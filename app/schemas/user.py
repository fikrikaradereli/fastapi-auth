from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr | None = None


class User(UserBase):
    id: int
    full_name: str | None = None
    is_active: bool = True
    is_superuser: bool = False
    hashed_password: str
    created_at: datetime

    class Config:
        from_attributes = True


class UserCreate(UserBase):
    password: str


class UserLogin(UserBase):
    hashed_password: str
