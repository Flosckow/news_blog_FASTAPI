from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from news import schemas, models, views
from fastapi import FastAPI, Request


router = APIRouter()


@router.post("/add/", status_code=201, response_model=schemas.NewsCreate)
async def create_news(item: schemas.NewsCreate):
    return await views.create_news(item=item)


@router.get("/all/", response_model=List[schemas.NewsGet])
async def get_all_news():
    return await views.get_all_news()


@router.delete("/delete/{news_id}", status_code=204)
async def delete_news(news_id: int):
    return await views.delete_news(news_id)


@router.post('/{news_id}/add_comment/', status_code=201, response_model=schemas.CommentCreate)
async def create_comment(item: schemas.CommentCreate, news_id: int, author_id: int):
    return await views.add_post_comment(item=item, news_id=news_id, author_id=author_id)


@router.get('/{news_id}/view_comment/', response_model=List[schemas.CommentGet])
async def get_all_comment(news_id: int):
    return await views.get_all_comment_for_news(news_id)


@router.get('/one_news/{news_id}/', response_model=schemas.NewsGet)
async def get_one_news(news_id: int):
    return await views.get_one_news(news_id)


# @router.get("/author/comment/", response_model=schemas.UserComment)
# async def comment_author():
#     return await views.get_comment_author()

@router.post("/add/review/", response_model=schemas.CreateReview, status_code=201)
async def create_review(item: schemas.CreateReview, comment_id: int, author_id: int):
    return await views.create_review(item=item, comment_id=comment_id, author_id=author_id)


# сделать количество выводимых постов, например 50, с последующей подгрузкой
@router.get("/all/reviews/{comment_id}/", response_model=List[schemas.GetReview])
async def get_all_review_comment(comment_id: int):
    return await views.get_review_for_comment(comment_id)


@router.delete("/delete/review/{review_id}")
async def delete_review(review_id: int):
    return await views.delete_review(review_id)