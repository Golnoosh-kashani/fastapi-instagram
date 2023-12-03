from sqlalchemy.orm import Session
from db.models.users import User
from schemas.comments import Comment_input
from db.models.comments import Comment
from db.models.posts import Post
def create_comment(post_id:int,comment_data:Comment_input,current_user:User,db:Session):
    new_comment=Comment(text=comment_data.text,user_id=current_user.id,post_id=post_id)
    db.add(new_comment)
    db.commit()
    return new_comment

def delete_comment(user_id:int,post_id:int,comment_id:int,current_user:User,db:Session):
    #check user is writer of comment
    if current_user.id==user_id:
        comment_delete=db.query(Comment).filter(Comment.id==comment_id,Comment.post_id==post_id)
    else:
        return False  
    #ckeck if comment_delete return none  
    if comment_delete is None:
        return False
    else:
        db.delete(comment_delete)
        db.commit()
        return True
    

    #get all post's comments
def show_post_comments(post_id:int,db:Session):
    get_comments=db.query(Post.comments).all()
    if get_comments:
        return get_comments
    else:
        return False    

    