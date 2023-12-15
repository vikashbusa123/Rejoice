from sqlalchemy.orm import Session
from .. import models,schemas
from fastapi import HTTPException,status




def get_all(db:Session):
    blogs=db.query(models.Blog).all()
    return blogs

def create(request:schemas.RequestBlog,db:Session):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
def destroy(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id,request:schemas.RequestBlog,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    
    if blog.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id {id} not found")
    #print(request)
    print("BCD")
    print(type(request))
    blog.update(dict(request))
    print(type(request))
    print("CC")
    db.commit()
    return 'updated'

def show(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available")
        #response.status_code=status.HTTP_404_NOT_FOUND
        #return {'details':f"Blog with the id {id} is not available"}
    return blog 
