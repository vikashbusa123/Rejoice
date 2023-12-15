from sqlalchemy.orm import Session
from .. import models,schema,outh2,database
from fastapi import HTTPException,status,Depends
get_db=database.get_db



def get_all(db:Session):
    comments=db.query(models.CommentModel).all()
    return comments
    
def create(post_id,current_user,request:schema.Requestcomment,db:Session=Depends(get_db)):
    print(current_user.id)
    
    post=db.query(models.PostMetadata).filter(models.PostMetadata.id==post_id).first()
    user=db.query(models.User).filter(models.User.id==current_user.id).first()
    
    if post :
        new_comment=models.CommentModel(post_id=post.id,user_id=user.id,comment=request.comment)
        db.add(new_comment)
        post.Number_of_comments=post.Number_of_comments+1
        db.commit()
        return new_comment
    
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {post_id} not found")

          
    
        
def destroy(id:int,db:Session):
    #breakpoint()
    comment=db.query(models.CommentModel).filter(models.CommentModel.id==id)
    if not comment.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Comment with id {id} not found")
    # print(post_id)
    #print(post_id)
    # print("A")
    # print(comment)
    post=db.query(models.PostMetadata).filter(models.PostMetadata.id==comment.first().post_id).first()
    print(post.Number_of_comments)
    post.Number_of_comments=post.Number_of_comments-1
    comment.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id,request:schema.Requestcomment,db:Session):
    comment=db.query(models.CommentModel).filter(models.CommentModel.id == id)
    if comment.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"comment with id {id} not found")
    print(request)
    comment.update(request)
    db.commit()
    return 'updated'

def show(id:int,db:Session):
    comment=db.query(models.CommentModel).filter(models.CommentModel.id==id).first()
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Comment with the id {id} is not available")
        #response.status_code=status.HTTP_404_NOT_FOUND
        #return {'details':f"Blog with the id {id} is not available"}
    return comment
