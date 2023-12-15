from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from .. import database,schemas,models
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..repository import user
router=APIRouter(
    prefix="/user",
    tags=['Users']
)
get_db=database.get_db


@router.post('/',response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    # new_user=models.User(name=request.name,email=request.email,password=Hash.bcreypt(request.password))
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)
    # return new_user
    return user.create(request,db)

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db:Session=Depends(get_db)):
    # user=db.query(models.User).filter(models.User.id == id).first()
    # if not user:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"User with the id {id} is not available")
    # return user
    return user.show(id,db)


@router.delete('/{id}')
def destroy(id:int,db:Session=Depends(get_db)):
    return user.destroy(id,db)