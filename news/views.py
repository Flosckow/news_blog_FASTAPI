from pprint import pprint

from . import schemas
from db.session import database
from sqlalchemy import select, text
from .models import news, comment
from users.models import users
from fastapi import FastAPI, Request


async def create_news(item: schemas.NewsCreate):
    news_create = item.dict(exclude={'comment'})
    news_pk = await database.execute(query=news.insert(), values=news_create)

    return {**item.dict(), 'id': news_pk}


# переработать эту функцию для присваивания id пользователя
async def add_post_comment(item: schemas.CommentCreate, news_id: int, author_id: int):
    comm = comment.insert().values(**item.dict(), news_id=news_id, author_id=author_id)
    comm_pk = await database.execute(comm)
    return {**item.dict(), 'id': comm_pk, "news_id": {"id": news_id}, "author_id": {"id": author_id}}


async def delete_news(pk: int):
    new = news.delete().where(news.c.id == pk)
    return await database.execute(new)


async def get_all_news():
    n = news.alias('news')
    q = select([n])

    news_list = await database.fetch_all(query=q)

    on_lst = [dict(su) for su in news_list]

    return on_lst


async def get_all_comment_for_news(pk: int):
    comm = comment.alias('comm')
    q = select([comm.join(news).join(users)]).where(news.c.id == pk)
    comment_list = await database.fetch_all(q)

    on_lst = [dict(su) for su in comment_list]

    return on_lst

