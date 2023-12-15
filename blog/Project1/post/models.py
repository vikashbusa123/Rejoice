from datetime import datetime
from sqlalchemy import Column, ForeignKey,Integer,String,DateTime
from .database import Base
from sqlalchemy.orm import relationship 


class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)
    #post_id=Column(Integer,ForeignKey("Posts.id"))
    posts=relationship("PostMetadata",back_populates="user")


class PostMetadata(Base):
    
    __tablename__="Posts"
    id=Column(Integer, primary_key=True)
    location=Column(String)
    photo=Column(String,nullable=False)
    caption=Column(String)
    upload_time=Column(DateTime, default=datetime.now())
    Number_of_like=Column(Integer,default=0)
    Number_of_comments=Column(Integer,default=0)
    #comment_id=Column(Integer, ForeignKey('Comments.id'))
    comments=relationship('CommentModel', back_populates='post')   
     
    user_id = Column(Integer, ForeignKey('users.id'))
    user=relationship("User",back_populates="posts")
    
    likes=relationship('LikeModel',back_populates='post1')
    
        
class CommentModel(Base):
    
    __tablename__='Comments'
    id=Column(Integer,primary_key=True)
    comment=Column(String)
    post_id = Column(Integer,ForeignKey("Posts.id"))
    user_id=Column(Integer,ForeignKey("users.id"))
    
    post=relationship("PostMetadata",back_populates="comments")
    
class LikeModel(Base):
    __tablename__='Like'
    id=Column(Integer,primary_key=True)
    post_id=Column(Integer,ForeignKey("Posts.id"))
    user_id=Column(Integer,ForeignKey("users.id"))
    post1=relationship("PostMetadata",back_populates="likes")

    # filename=Column(String)
    # filepath=Column(String)
    
