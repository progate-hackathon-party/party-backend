import os
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute,NumberAttribute
from pydantic import BaseModel
from typing import Optional

class UserModel(Model):
    # 接続先情報(クレデンシャルやテーブル情報)を定義
    class Meta:
        table_name = "users"
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
    # テーブル属性定義
    id = UnicodeAttribute(hash_key=True)
    user_id = UnicodeAttribute(null=False)
    name = UnicodeAttribute(null=False)
    content = UnicodeAttribute(null=False)
    lat = NumberAttribute()  # 緯度
    lon = NumberAttribute()
    image_url = UnicodeAttribute(null=False)

class Post(BaseModel):
    id: Optional[str] = None
    user_id: Optional[str] = None
    name: str
    content: str
    lat: float
    lon: float
    image_url: str