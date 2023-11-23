from typing import Optional,Text
from fastapi import UploadFile, File, Form,Depends
from uuid import uuid4
import os
import shutil
from db.models.posts import Post
from sqlalchemy.orm import Session
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
        new_post = Post(caption=caption,image_path=file_path,date_created=datetime.now().date, owner_id=owner_id)
   
    else:
        # No image is provided
        raise ValueError("An image file  must be provided")

    # Add the new post to the database
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post
