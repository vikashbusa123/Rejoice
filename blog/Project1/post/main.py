from fastapi import FastAPI,File,UploadFile,Depends,Form,HTTPException,status
from fastapi.responses import FileResponse
from . import models
import uuid
from .database import engine
from fastapi.staticfiles import StaticFiles
import os
from random import randint
from post import schema
from .database import get_db
from sqlalchemy.orm import Session
from typing import Annotated
from .routers import comment,post,user,authentication,like
models.Base.metadata.create_all(bind=engine)


#IMAGEDIR="images/"
app=FastAPI()

app.include_router(authentication.router)
app.include_router(post.router)
app.include_router(comment.router)
app.include_router(user.router)
app.include_router(like.router)

app.mount("/static", StaticFiles(directory="images"), name="images")


# @app.post('/upload')
# async def create_upload_file(location: Annotated[str, Form()], caption: Annotated[str, Form()],file: UploadFile,db:Session=Depends(get_db)):
    
#     file.filename=f"{uuid.uuid4()}.jpg"
#     contents=await file.read()
    
#     with open(f"{IMAGEDIR}{file.filename}","wb") as f:
#         f.write(contents)
        
#     photo_d=models.PostMetadata(location=location,caption=caption,photo=file.filename)
#     db.add(photo_d)
#     db.commit()
#     db.refresh(photo_d)
#     return photo_d
        
    
    
#     # return {"filename":file.filename}


# @app.get("/show")
# def all(db:Session=Depends(get_db)):
#     photo_d=db.query(models.PostMetadata).all()
#     return photo_d

# @app.get('/show/{id}',status_code=200)
# def show(id,db:Session=Depends(get_db)):
#     photo_d=db.query(models.CommentModel).filter(models.CommentModel.post_id==id).all()
#     if not photo_d:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Photo with the id {id} is not available")
#         #response.status_code=status.HTTP_404_NOT_FOUND
#         #return {'details':f"photo with the id {id} is not available"}
#     return photo_d 






# @app.post('/comment/{id}')
# def create_comment(id, request:schema.Commentschema,db:Session=Depends(get_db)):
#     comment1=models.CommentModel(post_id=id,comment=request.comment)
#     db.add(comment1)
#     db.commit()
#     db.refresh(comment1)
#     return comment1

# @app.get('/comment/{id}')
# def get_comment(id:int,db:Session=Depends(get_db)):
#     comment1=db.query(models.CommentModel).filter(models.CommentModel.id == id).first()
#     if not comment1:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                            detail=f"comment with the id {id} is not available")
#     return comment1