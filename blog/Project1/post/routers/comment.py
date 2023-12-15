from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from .. import schema,database,models,outh2
from sqlalchemy.orm import Session
from ..Repository import comment


router=APIRouter(
    prefix="/comments",
    tags=['Comments']
)
get_db=database.get_db

@router.get('/',response_model=List[schema.Showcomment])
def all(db:Session=Depends(get_db),current_post:schema.postschema=Depends(outh2.get_current_user)):
    # blogs=db.query(models.Blog).all()
    # return blogs
    return comment.get_all(db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy_comment(id:int,db:Session=Depends(get_db),current_user:schema.postschema=Depends(outh2.get_current_user)):
    # blog=db.query(models.Blog).filter(models.Blog.id==id)
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"Blog with id {id} not found")
    # blog.delete(synchronize_session=False)
    # db.commit()
    # return 'done'
    return comment.destroy(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request:schema.Requestcomment, db:Session=Depends(get_db),current_user:schema.postschema=Depends(outh2.get_current_user)):
    # blog=db.query(models.Blog).filter(models.Blog.id == id)
    # if blog.first() is None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id {id} not found")
    # blog.update(request)
    # db.commit()
    # return 'updated'
    return comment.update(id,request,db)

@router.post('/{id}',status_code=status.HTTP_201_CREATED)
def create(id:int,request:schema.Commentschema,db:Session=Depends(get_db),current_user=Depends(outh2.get_current_user)):
    # new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    # db.add(new_blog)
    # db.commit()
    # db.refresh(new_blog)
    # return new_blog
   
   
    return comment.create(id,current_user,request,db)


@router.get('/{id}',status_code=200,response_model=schema.Showcomment)
def show(id:int,db:Session=Depends(get_db),current_user:schema.postschema=Depends(outh2.get_current_user)):
    # blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    # if not blog:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available")
    #     #response.status_code=status.HTTP_404_NOT_FOUND
    #     #return {'details':f"Blog with the id {id} is not available"}
    # return blog 
    return comment.show(id,db)