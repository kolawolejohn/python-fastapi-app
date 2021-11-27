from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

from pydantic.types import conint


class PostBase(BaseModel):
   title: str
   content: str
   published: bool = True

class PostCreate(PostBase):
   pass


class User(BaseModel): ## response Model
   id: int
   email: EmailStr
   created_at:datetime

   class Config:
      orm_mode = True
class Post(PostBase):
   id: int
   created_at: datetime
   owner_id: int
   owner: User

   class Config:
      orm_mode = True

##Not sure if he noticed it or not, but @ 10:26:02 - I think what fixed the issue was making the PostVote class extend BaseModel instead of Post. (ie: PostVote(BaseModel))
class PostVote(BaseModel):
   Post: Post
   votes: int

   class Config:
      orm_mode = True

class UserCreate(BaseModel): ##request Model
   email: EmailStr
   password: str


class UserLogin(BaseModel):
   email: EmailStr
   password: str

   class Config:
      orm_mode = True


class Token(BaseModel):
   access_token: str
   token_type: str


class TokenData(BaseModel):
   id: Optional[str] = None


class Vote(BaseModel):
   post_id: int
   dir: conint(le=1)