from datetime import datetime
from typing import Optional
from pydantic import EmailStr
from sqlmodel import SQLModel, Field, Column, String
from sqlalchemy import DateTime
from sqlalchemy.sql import func

class ResourceBase(SQLModel):
    user_id: int =  Field(foreign_key="user.id")
    course_id: int = Field(foreign_key="course.id")
    description: str 
    url: str
    is_private: bool
    upload_date: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now()))



class ResourceCreate(ResourceBase):
    pass


class ResourceCreateReturn(ResourceBase):
    id :int


class ResourceRead(ResourceBase):
    id:int


class ResourceUpdate(SQLModel):
    description: Optional[str] = None



