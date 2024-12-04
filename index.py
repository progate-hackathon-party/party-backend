from fastapi import FastAPI
import uvicorn
from lib.users import get_user, get_user_by_id, create_user, update_user
from lib.posts import get_posts, get_post_by_id, create_post, delete_post

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Pong!!"}

# Users
@app.get("/users") 
async def root():
    result = get_user()
    return result

@app.get("/users/{user_id}")
async def root(user_id: str):
    result = get_user_by_id(user_id)
    return result

@app.post("/users")
async def root():
    result = create_user()
    return result

@app.put("/users")
async def root():
    result = update_user()
    return result


# Posts
@app.get("/posts")
async def root():
    result = get_posts()
    return result

@app.get("/posts/{post_id}")
async def root(post_id: str):
    result = get_post_by_id(post_id)
    return result

@app.post("/posts")
async def root():
    result = create_post()
    return result

@app.delete("/posts")
async def root():
    result = delete_post()
    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000, log_level="debug")

