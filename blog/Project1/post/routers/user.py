from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from .. import database,schema,models,outh2
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..Repository import user
router=APIRouter(
    prefix="/user",
    tags=['Users']
)
get_db=database.get_db


@router.post('/',response_model=schema.ShowUser)
def create_user(request:schema.User,db:Session=Depends(get_db)):
    # new_user=models.User(name=request.name,email=request.email,password=Hash.bcreypt(request.password))
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)
    # return new_user
    return user.create(request,db)

@router.get('/{id}',response_model=schema.ShowUser)
def get_user(id:int,db:Session=Depends(get_db)):
    # user=db.query(models.User).filter(models.User.id == id).first()
    # if not user:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"User with the id {id} is not available")
    # return user
    return user.show(id,db)


@router.delete('/{id}')
def destroy(id:int,db:Session=Depends(get_db),current_post:schema.postschema=Depends(outh2.get_current_user)):
    return user.destroy(id,db)