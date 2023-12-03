from sqlalchemy.orm import Session
from db.models.users import User
from schemas.comments import Comment_input
from db.models.comments import Comment
def create_comment(comment_data:Comment_input,current_user:User,db:Session):
    new_comment=Comment()