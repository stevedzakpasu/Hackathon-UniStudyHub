from datetime import datetime
from typing import Optional
from pydantic import EmailStr
from sqlmodel import Relationship, SQLModel, Field, Column, String
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from app.models.category import Category
from app.models.course import Course

from app.models.user import User

class ResourceBase(SQLModel):
    user_id: int =  Field(foreign_key="user.id")
    course_id: int = Field(foreign_key="course.id")
    description: str 
    url: str
    upload_date: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now()))
    image_url: Optional[str]
    user: User = Relationship(back_populates="resource")
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")
    category: Category = Relationship(back_populates="resource")
    course: Course = Relationship(back_populates="resource")


class ResourceCreate(ResourceBase):
    pass


class ResourceCreateReturn(ResourceBase):
    id :int


class ResourceRead(ResourceBase):
    id:int


class ResourceUpdate(SQLModel):
    description: Optional[str] = None



