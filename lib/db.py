import os
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
from pynamodb.connection import Connection

load_dotenv(".env")

connection = Connection(
    region=os.environ.get("REGION"),
    aws_access_key_id=os.environ.get("ACCESS_KEY_ID"),
    aws_secret_access_key=os.environ.get("ACCESS_SECRET_KEY")
)

class UserModel(Model):
    # 接続先情報(クレデンシャルやテーブル情報)を定義
    class Meta:
        table_name = "users"
        region=os.environ.get("REGION"), # リージョン指定
        host = os.environ.get("DYNAMO_DB_HOST") # ローカルDynamoDBの場合はホスト指定
        connection = connection
    # テーブル属性定義
    id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute(null=False)
    email = UnicodeAttribute(null=False)
    
class User(BaseModel):
    id: Optional[str] = None
    email: str


class PostModel(Model):
    class Meta:
        table_name = "posts"
        region=os.environ.get("REGION"), # リージョン指定
        host = os.environ.get("DYNAMO_DB_HOST") # ローカルDynamoDBの場合はホスト指定
        connection = connection
    # テーブル属性定義
    id = UnicodeAttribute(hash_key=True)
    user_id = UnicodeAttribute(null=False)
    content = UnicodeAttribute(null=False)
    location = UnicodeAttribute(null=False)
    image_url = UnicodeAttribute(null=False)

class Post(BaseModel):
    id: Optional[str] = None
    user_id: Optional[str] = None
    content: str
    location: str
    image_url: str