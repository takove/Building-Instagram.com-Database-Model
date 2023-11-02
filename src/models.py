import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
from sqlalchemy.sql import func

time_created = Column(DateTime(timezone=True), server_default=func.now())
time_updated = Column(DateTime(timezone=True), onupdate=func.now())

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    phone_number = Column(String(60))
    email = Column(String(60), nullable=False)
    username = Column(String(60), nullable=False)
    password = Column(String(60), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    follower = relationship("Follower")
    favorites = relationship("Favorites")
    comment = relationship("Comment")
    post = relationship("Post")

    def follower(self):
        return None
    
    def update(self):
        return None


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    media = relationship("Media")
    favorites = relationship("Favorites")

    def update(self):
        return None


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    content = Column(String(260), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    favorites = relationship("Favorites")

    def update(self):
        return None


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    url = Column(String(260), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    favorites = relationship("Favorites")

    def update(self):
        return None


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    comment_id = Column(Integer, ForeignKey('comment.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def update(self):
        return None
    

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    id_from_user = Column(Integer, ForeignKey('user.id'), nullable=False)
    id_to_user = Column(Integer, ForeignKey('user.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def update(self):
        return None

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')