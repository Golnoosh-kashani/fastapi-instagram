from typing import Optional,Text
from fastapi import UploadFile, File, Form,Depends,HTTPException
from uuid import uuid4
import os
import shutil
from db.models.posts import Post
from sqlalchemy.orm import Session
from db.models.users import User
from db.session import get_db
from datetime import datetime
async def create_new_post(db: Session, owner_id, image: Optional[UploadFile] = File(...),caption: Text = Form(...)):
    if image:
        # Image file is uploaded
        filename = f"{uuid4()}-{image.filename}"
        file_path = f"images/{filename}"

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        
        # Create a new Posts instance with the file path and caption
        new_post = Post(caption=caption,image_path=file_path,date_created=datetime.now(), owner_id=owner_id)
   
    else:
        # No image is provided
        raise ValueError("An image file  must be provided")

    # Add the new post to the database
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


def delete_post_by_id(post_id:int,db:Session,current_user:User):
    post=db.query(Post).filter(Post.id==post_id).first()
    
    # Check if the post exists
    if not post:
        return False

    # Check if the current user is the owner of the post
    if current_user.id != post.owner_id:
        return False

    try:
        # Delete post image
        os.remove(post.image_path)
    except OSError as e:
        print(f"A OSError occurred: {e}")

    # Delete the post from the database and commit the transaction
    db.delete(post)
    db.commit()
    return True

def update_post_by_id(post_id:int,new_post_data:dict,db:Session):
    post=db.query(Post).filter(Post.id==post_id)
    if post:
        # update post data and skip date_created attribute
        for key,value in post:
            if key != 'date_created' and hasattr(post,key):
                setattr(post,key,value)

        db.commit()
        return(f"User with ID {post_id} has been updated.")

def get_all_user_posts(owner_id:int,db:Session):
    get_all_posts=db.query(Post).filter(Post.owner_id==owner_id).all()
    return get_all_posts