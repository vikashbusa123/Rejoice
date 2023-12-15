from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from .. import schemas,database,models,outh
from sqlalchemy.orm import Session
from ..repository import blog


router=APIRouter(
    prefix="/blog",
    tags=['Blogs']
)
get_db=database.get_db

@router.get('/',response_model=List[schemas.ShowBlog])
def all(db:Session=Depends(get_db),current_user:schemas.User=Depends(outh.get_current_user)):
    # blogs=db.query(models.Blog).all()
    # return blogs
    return blog.get_all(db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session=Depends(get_db),current_user:schemas.User=Depends(outh.get_current_user)):
    # blog=db.query(models.Blog).filter(models.Blog.id==id)
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"Blog with id {id} not found")
    # blog.delete(synchronize_session=False)
    # db.commit()
    # return 'done'
    return blog.destroy(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request:schemas.RequestBlog, db:Session=Depends(get_db),current_user:schemas.User=Depends(outh.get_current_user)):
    # blog=db.query(models.Blog).filter(models.Blog.id == id)
    # if blog.first() is None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id {id} not found")
    # blog.update(request)
    # db.commit()
    # return 'updated'
    print("B")
   
    return blog.update(id,request,db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.RequestBlog,db:Session=Depends(get_db),current_user:schemas.User=Depends(outh.get_current_user)):
    # new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    # db.add(new_blog)
    # db.commit()
    # db.refresh(new_blog)
    # return new_blog
    return blog.create(request,db)


@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def show(id:int,db:Session=Depends(get_db),current_user:schemas.User=Depends(outh.get_current_user)):
    # blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    # if not blog:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available")
    #     #response.status_code=status.HTTP_404_NOT_FOUND
    #     #return {'details':f"Blog with the id {id} is not available"}
    # return blog 
    return blog.show(id,db)