from typing import Optional

from passlib.context import CryptContext
from re import *

from sqlalchemy import select

from users.models import User, users

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    return pwd_context.hash(password)





# def get_address(address):
#     pattern = compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
#     is_valid = pattern.match(address)
#     if is_valid:
#         print('правильный email:', is_valid.group())
#         # объект is_valid содержит 3 метода
#         print('методы: start:', is_valid.start(), 'end:',\
#         is_valid.end(), 'group:', is_valid.group())
#     else:
#         print('неверный email! введите email...\n')