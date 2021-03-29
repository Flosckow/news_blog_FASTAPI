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
    return await views.get_all_cooment_for_news(news_id)