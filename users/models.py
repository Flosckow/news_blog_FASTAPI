from db.session import Base
from sqlalchemy import Column, String, Integer, Boolean


class User(Base):
    __tablename__ = 'users_table'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)


users = User.__table__