import uuid
from typing import Optional, List
from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    hashed_password: str
    is_active: bool
    is_superuser: bool


class UserGet(UserBase):
    id: int
    pass


class UserUpdate(UserBase):
    pass


class UserComment(UserBase):
    pass


