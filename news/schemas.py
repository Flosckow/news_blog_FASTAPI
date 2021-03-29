import uuid
from typing import Optional, List
import pydantic
from pydantic import BaseModel
from users.schemas import *
from datetime import datetime


class CommentBase(BaseModel):
    body_c: str

    # author: UserComment

    class Config:
        orm_mode = True


class NewsBase(BaseModel):
    """Base model schemas News"""
    head: str
    body: str

    class Config:
        orm_mode = True


class NewsCreate(NewsBase):
    pass


class CommentGet(CommentBase):
    pass


class NewsGet(NewsBase):
    id: int
    date: datetime
    # comment: List[CommentGet]  # = []


class NewsDelete(NewsBase):
    id: int


class NewsUpdate(NewsBase):
    id: int
    comment: List[CommentBase]


class CommentCreate(CommentBase):
    pass
    # news_id: int
    # author: UserComment

