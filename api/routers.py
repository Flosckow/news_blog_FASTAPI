from fastapi import APIRouter

from api.endpoint import news, users

api_router = APIRouter()

api_router.include_router(news.router, tags=["blog"])
api_router.include_router(users.router, tags=["users"])