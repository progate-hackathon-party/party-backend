from lib.db import UserModel,User

def get_user():
    try:
        user = UserModel.get("1")
        return {"users": [user.name, user.email]}
    except:
        return {"Error":"User not found"}

def get_user_by_id(user_id: str):
    try:
        user = UserModel.get(user_id)
        return {"user": user}
    except:
        return {"Error":"User not found"}

def create_user():
    try:
        user = User(id="1", email="", name="")
        user.save()
        return {"message": "User created successfully"}
    except:
        return {"Error":"User not created"}

def update_user():
    try:
        user = UserModel.get("1")
        user.email = "mona.hiro@monaka.org"
        user.name = "John Doe"
        user.save()
        return {"message": "User updated"}
    except:
        return {"Error":"User not updated"}