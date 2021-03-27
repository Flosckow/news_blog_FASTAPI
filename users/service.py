from typing import Optional

from sqlalchemy.orm import Session

from users.models import User, users
from users.schemas import UserCreate, UserUpdate, UserGet
from core.security import verify_password, get_password_hash
from db.session import database
from sqlalchemy import select, text


async def get_all_users():
    u = users.alias('user')
    q = select([u])

    user_list = await database.fetch_all(q)

    on_list = [dict(u) for u in user_list]

    return on_list


async def get_user_by_id(pk: int):
    u = users.alias('user')
    q = select([u]).where(u.c.id == pk)
    user = await database.fetch_one(q)
    if user is not None:
        user = dict(user)
        return {**user}
    return None


async def create_user(item: UserCreate):
    hashed_password = get_password_hash(item.hashed_password)
    item.hashed_password = hashed_password
    user_create = item.dict()
    user_pk = await database.execute(query=users.insert(), values=user_create)

    return {**item.dict(), 'id': user_pk}
