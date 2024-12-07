from lib.db import PostModel,Post

def get_posts():
    try:
        posts = PostModel.scan()
        return {"posts": [post.content for post in posts]}
    except:
        return {"Error":"Posts not found"}

def get_post_by_id(post_id: str):
    try:
        post = PostModel.get(post_id)
        return {
            "id": post.id,
            "user_id": post.user_id,
            "content": post.content,
            "position": post.position,
            "image_url": post.image_url
        }
    except:
        return {"Error":"Post not found"}

def create_post():
    try:
        post = Post(id="1", user_id="", content="", position="", image_url="")
        post.save()
        return {"message": "Post created successfully"}
    except:
        return {"Error":"Post not created"}

def delete_post():
    try:
        post = PostModel.get("1")
        post.delete()
        return {"message": "Post deleted successfully"}
    except:
        return {"Error":"Post not deleted"}