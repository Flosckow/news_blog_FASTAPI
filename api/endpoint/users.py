from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from users import schemas, models, service

router = APIRouter()


@router.get("/all/users/", response_model=List[schemas.UserGet])
async def all_user():
    return await service.get_all_users()


@router.get("/users/user_id/", response_model=schemas.UserGet)
async def get_one_user(user_id: int):
    return await service.get_user_by_id(user_id)


@router.post("/create/users/", status_code=201, response_model=schemas.UserCreate)
async def user_create(item: schemas.UserCreate):
    return await service.create_user(item=item)


@router.post("/authenticate/user/", status_code=201, response_model=schemas.UserLogin)
async def user_login(item: schemas.UserLogin):
    return await service.authenticate(email=item.email, password=item.hashed_password)


