from typing import List
from pydantic import BaseModel


class RequestBlogbase(BaseModel):
    title:str
    body:str
class RequestBlog(RequestBlogbase):
    class Config():
        orm_mode=True

        
        
class User(BaseModel):
    name:str 
    email:str
    password:str
    
class ShowUser(BaseModel):
    name:str
    email:str
    blogs:List[RequestBlog]=[]
    
        
class ShowBlog(BaseModel):
    title:str
    body:str
    creator:ShowUser
    class Config():
        orm_mode=True
        
class Login(BaseModel):
    username:str
    password:str
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
