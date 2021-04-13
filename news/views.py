from . import schemas
from db.session import database
from sqlalchemy import select
from .models import news, comment, review
from users.models import users
from fastapi import HTTPException


async def create_news(item: schemas.NewsCreate):
    news_create = item.dict(exclude={'comment'})
    news_pk = await database.execute(query=news.insert(), values=news_create)

    return {**item.dict(), 'id': news_pk}


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


async def get_one_news(pk: int):
    n = news.alias('news')
    q = select([n]).where(news.c.id == pk)
    news_one = await database.fetch_one(q)
    if not news_one:
        raise HTTPException(status_code=404, detail="Item not found")
    return dict(news_one)


# изменить передаваемые параметры коммента и автора, должны передаваться динамически
async def create_review(item: schemas.CreateReview, comment_id: int, author_id: int):
    reviews = review.insert().values(**item.dict(), comment_id=comment_id, author_id=author_id)
    reviews_pk = await database.execute(reviews)
    return {**item.dict(), 'id': reviews_pk, comment_id: {"id": comment_id}, "author_id": {"id": author_id}}


async def get_review_for_comment(pk: int):
    q = select([review.join(comment).join(users)]).where(comment.c.id == pk)
    reviews_list = await database.fetch_all(q)

    on_lst = [dict(rev) for rev in reviews_list]

    return on_lst


async def delete_review(pk : int):
    reviews = review.delete().where(review.c.id == pk)
    return await database.execute(reviews)


