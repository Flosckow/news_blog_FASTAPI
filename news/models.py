from sqlalchemy.orm import relationship
from db.session import Base

from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, sql
from users.models import User


class News(Base):
    __tablename__ = 'news_table'
    id = Column(Integer, primary_key=True, index=True)
    head = Column(String)
    body = Column(String(350))
    date = Column(DateTime(timezone=True), server_default=sql.func.now())


news = News.__table__


class Comment(Base):
    __tablename__ = 'comments_table'
    id = Column(Integer, primary_key=True, index=True)
    body_c = Column(String)
    news = relationship("News", backref='comments')
    news_id = Column(Integer, ForeignKey('news_table.id', ondelete="CASCADE"))
    author = relationship("User", backref="author")
    author_id = Column(Integer, ForeignKey('users_table.id', ondelete="CASCADE"))
    date = Column(DateTime(timezone=True), server_default=sql.func.now())


comment = Comment.__table__


class Review(Base):
    __tablename__ = 'review_table'
    id = Column(Integer, primary_key=True, index=True)
    body_r = Column(String(350))
    comments = relationship("Comment", backref="review")
    comment_id = Column(Integer, ForeignKey('comments_table.id', ondelete="CASCADE"))
    author = relationship("User", backref="author")
    author_id = Column(Integer, ForeignKey('users_table.id', ondelete="CASCADE"))
    date = Column(DateTime(timezone=True), server_default=sql.func.now())


review = Review.__table__