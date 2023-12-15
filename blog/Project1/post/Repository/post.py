from sqlalchemy.orm import Session
from .. import models,schema
from fastapi import Depends, HTTPException,status,UploadFile,File
from ..hashing import Hash
from ..database import get_db
from fastapi.responses import FileResponse


# def create(request:schema.postschema,db:Session):
#     new_post=models.PostMetadata(location=request.location,caption=request.caption,photo=file.filename)
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
#     return new_post
    
    
def show(id:int,db:Session):
    breakpoint()
    post=db.query(models.PostMetadata).filter(models.PostMetadata.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with the id {id} is not available")
    return post

def destroy(id:int,db:Session):
    post=db.query(models.PostMetadata).filter(models.PostMetadata.id == id)
    # breakpoint()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with the id {id} is not available")
    post.delete()
    db.commit()
    return 'done'