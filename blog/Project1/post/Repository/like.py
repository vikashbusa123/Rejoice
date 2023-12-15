from fastapi import Depends,HTTPException,status
from sqlalchemy.orm import Session
from .. import schema,database,models
get_db=database.get_db



def create(post_id,current_user,db:Session=Depends(get_db)):
    
    
    post=db.query(models.PostMetadata).filter(models.PostMetadata.id==post_id).first()
    user=db.query(models.User).filter(models.User.id==current_user.id).first()
    # breakpoint()
    # liked_user=[]
    user_liked_on_post = db.query(models.LikeModel).filter(models.LikeModel.post_id==post_id).filter(models.LikeModel.user_id==current_user.id).all()

    if user_liked_on_post:
        # remove the like
        delete_like=db.query(models.LikeModel).filter(models.LikeModel.post_id==post_id)
        delete_like.delete()
        db.commit()
        # get the post
        #breakpoint()
    
        post=db.query(models.PostMetadata).filter(models.PostMetadata.id==post_id).first()
        # update the like count
        post.Number_of_like = post.Number_of_like - 1
        #print(post.id)
        
       # post.Number_of_like = post.Number_of_like - 1
        db.commit()
        return " updated If"
    else:
        # add the like 
        like=models.LikeModel(post_id=post.id,user_id=user.id)

        db.add(like)
        db.commit()
        # get the user
        post=db.query(models.PostMetadata).filter(models.PostMetadata.id==post_id).first()
        post.Number_of_like = post.Number_of_like + 1

        db.commit()
        return " updated Else"
        # user.update(likes = post.likes - 1)
        # UPDATE THE COUNT 
    
    # if post:
    #     liked_user=[]    
    #     liked=db.query(models.LikeModel).filter(models.LikeModel.post_id==post_id).all()
    #     for i in range(0,len(liked)):
    #         liked_user.append(liked[i].user_id)
    #     print(current_user.id)
    #     print(liked_user)
    #     if current_user.id in liked_user:
    #         delete_like=db.query(models.LikeModel).filter(models.LikeModel.post_id==post_id)
    #         delete_like.delete() 
    #         #like=models.LikeModel(post_id=post.id,user_id=user.id,like=request.like)

    #         #db.add(like)
    #         db.commit()
    #         return "done"
    #     else:
    #         like=models.LikeModel(post_id=post.id,user_id=user.id)

    #         db.add(like)
    #         db.commit()
    #         return "done"
    # else:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"Post with id {post_id} not found")
    # L=len(liked_user)
def destroy(id:int,db:Session):
    like=db.query(models.LikeModel).filter(models.LikeModel.id==id)
    if not like.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    like.delete(synchronize_session=False)
    db.commit()