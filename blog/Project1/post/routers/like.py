
from fastapi import APIRouter,status,Depends
from sqlalchemy.orm import Session
from .. import schema,outh2,database
from ..Repository import like
get_db=database.get_db

router=APIRouter(
    prefix="/likes",
    tags=['Likes']
)


@router.post('/{id}',status_code=status.HTTP_201_CREATED)
def create(id:int,db:Session=Depends(get_db),current_user=Depends(outh2.get_current_user)):
    return like.create(id,current_user,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session=Depends(get_db)):
    return like.destroy(id,db)