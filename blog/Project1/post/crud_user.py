from . import schema,models
from fastapi import Depends
from . import database
from sqlalchemy.orm import Session
get_db=database.get_db


# def get_by_id(self,db: Session=Depends(get_db), *,id: str) -> models.User:
#         db1=db.query(models.User).filter(models.User.id == id).first()
#         return db1

def get_by_id(id:str,db:Session=Depends(get_db)):
        db1=db.query(models.User).filter(models.User.id==id).first()
        return db1
