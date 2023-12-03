from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from core.routers.login_router import get_current_user
from db.models.users import User
from core.crud.comment_crud import create_comment,show_post_comments,delete_comment
from schemas.comments import Comment_input

router=APIRouter()

@router.post("posts/comment")
def CreateComment(post_id:int,comment_data:Comment_input,current_user:User=Depends(get_current_user),db:Session=Depends(get_db)):
    new_comment=create_comment(post_id=post_id,comment_data=comment_data,current_user=current_user,db=db)
    if new_comment:
        return{"comment posted"}

@router.get("/posts/{post_id}/comments")
def ShowComments(post_id:int,db:Session=Depends(get_db)):
    get_comments=show_post_comments(post_id=post_id,db=db)
    return get_comments

@router.delete("/posts/{post_id}/{comment_id}")
def DeleteComment(user_id:int,post_id:int,comment_id:int,current_user:User=Depends(get_current_user),db:Session=Depends(get_db)):
    
    try:
        deliting_comment=delete_comment(user_id=user_id,post_id=post_id,comment_id=comment_id,current_user=current_user,db=db)
        if deliting_comment:
            return {"message": "comment has been deleted"}
        else:
            raise HTTPException(status_code=403, detail="Not authorized to perform this action")
    except ValueError as e:  # Catching a more specific exception
        print(f"A ValueError occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")