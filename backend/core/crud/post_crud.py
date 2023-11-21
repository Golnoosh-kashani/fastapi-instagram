from typing import Optional
from fastapi import UploadFile, File, Form,Depends
from uuid import uuid4
import os
import shutil
from db.models.posts import Posts
from sqlalchemy.orm import Session
from db.session import get_db

async def create_new_post(db: Session=Depends(get_db), 
                          image: Optional[UploadFile] = File(None), 
                          image_url: Optional[str] = Form(None), 
                          caption: str = Form(...)):
    if image:
        # Image file is uploaded
        filename = f"{uuid4()}-{image.filename}"
        file_path = f"images/{filename}"

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        
        # Create a new Posts instance with the file path and caption
        new_post = Posts(image_path=file_path, caption=caption)
    elif image_url:
        # Image URL is provided instead of an uploaded file
        new_post = Posts(image_path=image_url, caption=caption)
    else:
        # No image or URL provided
        raise ValueError("An image file or image URL must be provided")

    # Add the new post to the database
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post
