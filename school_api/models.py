
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class BlogPost(BaseModel):
    id: str = Field(None, example="60c72b2f9b1e8a001c8c5f2a")  # Custom ID to represent the post
    title: str = Field(..., example="My First Blog Post")
    content: str = Field(..., example="This is the content of the blog post.")
    author: str = Field(..., example="Author Name")
    published: Optional[bool] = Field(default=False, example=True)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

    class Config:
        # Enable the model to be created from a MongoDB document
        arbitrary_types_allowed = True
        orm_mode = True  # Allows ORM model to Pydantic model conversion

