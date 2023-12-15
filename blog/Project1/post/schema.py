from typing import List,Optional,Generic,TypeVar
from pydantic import BaseModel,Field


T=TypeVar('T')

class Requestcommentbase(BaseModel):
    comment:str
    caption:str

class Requestcomment(Requestcommentbase):
    class Config():
        orm_mode=True
        
class Requestlikebase(BaseModel):
    pass
class Requestlike(Requestlikebase):
    class Config():
        orm_mode=True

class User(BaseModel):
    name:str 
    email:str
    password:str
    
class Commentschema(BaseModel):
    # profile_id:int
    #title:Optional[str]=None
    comment:Optional[str]=None
    
class postschema(BaseModel):
    location:str
    caption:str
    
class Login(BaseModel):
    username:str
    password:str
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    #email:str | None = None
    email:Optional[str]=None
    
    
    class Config:
        orm_mode=True
        
class ShowUser(BaseModel):
    name:str
    email:str
    blogs:List[Requestcomment]=[]


class Showcomment(BaseModel):
    id:int
    comment:str
    creator:ShowUser
    class Config():
        orm_mode=True
    #commentor:List[Requestcomment]=[]