from typing import List
import uuid
from fastapi import HTTPException
from pydantic import BaseModel
from lib.db import PostModel,Post

def get_posts():
    try:
        posts = PostModel.scan()
        return {"posts": [post for post in posts]}
    except:
        return {"Error":"Posts not found"}

def get_post_by_id(post_id: str):
    try:
        post = PostModel.get(post_id)
        return {
            "id": post.id,
            "user_id": post.user_id,
            "content": post.content,
            "location": post.location,
            "image_url": post.image_url
        }
    except:
        return {"Error":"Post not found"}

class PostLocation(BaseModel):
    lat: List[float]
    lon: List[float]
    
def get_posts_by_location(location:PostLocation):
    try:
        results = []

        for item in PostModel.scan():
            
            if location.lat[0] <= item.lat <= location.lat[1] and location.lon[0] <= item.lon <= location.lon[1]:
                results.append(item)
        

        return {"posts": results}
    except Exception as e:
        print(e)
        return {"Error":"Posts not found"}


def create_post(user_id:str,post:Post):
    try:
        #ここを実装
        uuid_string = uuid.uuid1()

        post = PostModel(id=str(uuid_string), user_id=user_id, name=post.name ,content=post.content, lat=post.lat,lon=post.lon, image_url=post.image_url)
        post.save()
        #成功したかしてないかを返す
        #コンテント、位置情報、画像のURL
        return {"message": "Post created successfully"}
    except:
        return {"Error":"Post not created"}

def delete_post(user_id:str,post_id:str):
    try:
        #ここを実装
        post = PostModel.get(post_id)

        if post.user_id == user_id:
            post.delete()
        else :
            raise HTTPException (status_code=401,detail = "Unauthorized")
        #消そうとしているユーザーが投稿の持ち主かどうか
        return {"message": "Post deleted successfully"}
    except:
        return {"Error":"Post not deleted"}