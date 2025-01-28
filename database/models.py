from sqlalchemy import (Column, String, Integer, Float,
                        DateTime, ForeignKey, Boolean)
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime
class User(Base):
    __tablename__ = 'Users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    phone_number = Column(String, unique=True)
    email = Column(String, unique=True)
    city = Column(String, nullable=True)
    password = Column(String)
    birthday = Column(String, nullable=True)
    reg_date = Column(DateTime, default=datetime.now())
    posts_fk = relationship("Post", back_populates="user_fk")

class Hashtags(Base):
    __tablename__ = 'Hashtags'
    hashtags_id = Column(Integer, primary_key=True)
    hashtag = Column(String, unique=True, nullable=False)

class Photo(Base):
    __tablename__ = 'Photos'
    photo_id = Column(Integer, primary_key=True, autoincrement=True)
    photo_path = Column(String, nullable=False)
    profile_photo = Column(Integer, ForeignKey('Users.user_id'), nullable=True)
    post_photo = Column(Integer, ForeignKey('posts.id'), nullable=True)
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    main_text = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    hashtag_id = Column(String, ForeignKey("hashtags.id"), nullable=True)
    post_date = Column(DateTime, default=datetime.now())
    user_fk = relationship(User, lazy="subquery",back_populates="post_fk" ,cascade="all, delete", passive_deletes=True)
    hashtag_fk = relationship(Hashtags, lazy="subquery")
class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    text = Column(String, nullable=False)
    user_fk = relationship(User, lazy="subquery")
    post_id = Column(Integer, ForeignKey("posts.id"))
    post_fk = relationship(Post, lazy="subquery")
    com_date = Column(DateTime, default=datetime.now())