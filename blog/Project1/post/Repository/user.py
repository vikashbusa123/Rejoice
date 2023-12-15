from sqlalchemy.orm import Session
from .. import models,schema
from fastapi import Depends, HTTPException,status
from ..hashing import Hash
from ..database import get_db

def create(request:schema.User,db:Session):
    new_user=models.User(name=request.name,email=request.email,password=Hash.bcreypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    
    
def show(id:int,db:Session):
    user=db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user

def destroy(id:int,db:Session):
    user=db.query(models.User).filter(models.User.id == id)
    # breakpoint()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    user.delete()
    db.commit()
    return 'done'