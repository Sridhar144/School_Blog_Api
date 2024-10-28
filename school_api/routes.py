from models import BlogPost
from fastapi import APIRouter, HTTPException

from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from get_database import db

router = APIRouter()

async def convert_ids(custom_id: str):
    post = await db.posts.find_one({"id": custom_id})

    if post:
        # If found, return the corresponding _id
        return str(post['_id'])  # Convert ObjectId to string for easier readability
    else:
        # Return None if no post is found
        return None
def convert_id(post):
    """Convert MongoDB ObjectId to custom string _id for responses."""
    # post['_id'] = str(post['id'])  # Add custom _id field
    # del post['id']  # Remove original ObjectId
    return post

@router.post("/posts/", response_description="Create a new blog post", response_model=BlogPost)
async def create_post(post: BlogPost):
    post_dict = jsonable_encoder(post)
    post_dict['created_at'] = datetime.utcnow()
    post_dict['updated_at'] = datetime.utcnow()
    new_post = await db.posts.insert_one(post_dict)
    created_post = await db.posts.find_one({"_id": new_post.inserted_id})
    return convert_id(created_post)

@router.get("/posts/", response_description="List all blog posts", response_model=list[BlogPost])
async def list_posts(skip: int = 0, limit: int = 10):
    posts = await db.posts.find().skip(skip).limit(limit).to_list(length=limit)
    return [convert_id(post) for post in posts]

@router.get("/posts/{post_id}", response_description="Get a single blog post", response_model=BlogPost)
async def get_post(post_id: str):
    # print(post_id)
    post_id = await convert_ids(post_id)
    # print(post_id)
    if not ObjectId.is_valid(post_id):
        raise HTTPException(status_code=400, detail="Invalid post _id")
    
    post = await db.posts.find_one({"_id": ObjectId(post_id)})
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    
    return convert_id(post)

@router.put("/posts/{post_id}", response_description="Update a blog post", response_model=BlogPost)
async def update_post(post_id: str, post: BlogPost):
    # print(post_id)
    post_id = await convert_ids(post_id)
    # print(post_id)
    if not ObjectId.is_valid(post_id):
        raise HTTPException(status_code=400, detail="Invalid post _id")

    update_data = jsonable_encoder(post)
    update_data['updated_at'] = datetime.utcnow()
    
    update_result = await db.posts.update_one({"_id": ObjectId(post_id)}, {"$set": update_data})
    
    if update_result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Post not found or no change made")

    updated_post = await db.posts.find_one({"_id": ObjectId(post_id)})
    return convert_id(updated_post)

@router.delete("/posts/{post_id}", response_description="Delete a blog post")
async def delete_post(post_id: str):
    # print(post_id)
    post_id = await convert_ids(post_id)
    # print(post_id)

    if not ObjectId.is_valid(post_id):
        raise HTTPException(status_code=400, detail="Invalid post _id")
    delete_result = await db.posts.delete_one({"_id": ObjectId(post_id)})
    
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Post not found")

    return {"message": "Post deleted successfully"}
