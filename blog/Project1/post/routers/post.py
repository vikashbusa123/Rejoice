from fastapi import APIRouter,Form,Depends,HTTPException,status,UploadFile
from typing import Annotated
import uuid
from .. import models,outh2,schema
from sqlalchemy.orm import Session
from ..database import get_db
from ..Repository import post
IMAGEDIR="images/"


router=APIRouter(
    prefix="/post",
    tags=['Posts']
)


@router.post('/upload')
async def create_upload_file(location: Annotated[str, Form()], caption: Annotated[str, Form()],file: UploadFile,db:Session=Depends(get_db),current_user=Depends(outh2.get_current_user)):
    
    file.filename=f"{uuid.uuid4()}.jpg"
    #breakpoint()
    contents=await file.read()
    with open(f"{IMAGEDIR}{file.filename}","wb") as f:
        f.write(contents)
    #print("uptil here")
    print(current_user.id)
    photo_d=models.PostMetadata(user_id=current_user.id, location=location,caption=caption,photo=file.filename)
    db.add(photo_d)
    db.commit()
    db.refresh(photo_d)
    return photo_d
    #return post.create(file,db)
        
    
    
    # return {"filename":file.filename}


@router.get("/show")
def all(db:Session=Depends(get_db),get_current_user:schema.postschema=Depends(outh2.get_current_user),current_post:schema.postschema=Depends(outh2.get_current_user)):
    posts=db.query(models.PostMetadata).all()
    return posts

@router.get('/show/{id}',status_code=200)
def show(id,db:Session=Depends(get_db)):
    # photo_d=db.query(models.CommentModel).filter(models.CommentModel.post_id==id).all()
    # if not photo_d:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Photo with the id {id} is not available")
    #     #response.status_code=status.HTTP_404_NOT_FOUND
    #     #return {'details':f"photo with the id {id} is not available"}
    # return photo_d 
    return post.show(id,db)

@router.delete('/{id}')
def destroy(id:int,db:Session=Depends(get_db),current_post:schema.postschema=Depends(outh2.get_current_user)):
    return post.destroy(id,db)


def update_like(id:int,db:Session=Depends(get_db)):
    likes=db.query(models.PostMetadata).filter(models.PostMetadata.Number_of_post==id).first()
    if not likes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    likes.update()
    db.commit()
    return likes
    