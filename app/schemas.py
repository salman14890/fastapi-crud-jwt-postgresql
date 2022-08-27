from pydantic import BaseModel, EmailStr
from datetime import datetime

class Create_Post(BaseModel):
    title: str
    content: str
    published: bool = True
    
class Update_Post(BaseModel):
    title: str
    content: str
    published: bool

class Create_User(BaseModel):
    email: EmailStr
    password: str

class Create_User_Response(BaseModel):
    id: int
    email: str
    created_at: datetime

    class Config():
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class Create_Vote(BaseModel):
    code_id:int
    dir:int 
    # dir 1 means like and dir 0 means dislike

