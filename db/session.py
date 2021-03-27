from sqlalchemy import create_engine
import databases
from core import config
from sqlalchemy.ext.declarative import declarative_base, declared_attr


class CustomBase:
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


engine = create_engine(config.SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False})
database = databases.Database(config.SQLALCHEMY_DATABASE_URI)
Base = declarative_base(cls=CustomBase)
