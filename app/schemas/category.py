from datetime import datetime
from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Relationship, SQLModel, Field, Column, String
from sqlalchemy import DateTime
from sqlalchemy.sql import func



class CategoryBase(SQLModel):
    name : str = Field(
        index=True, sa_column=Column("name", String, unique=True))


class CategoryCreate(SQLModel):
    name : str = Field(
        index=True, sa_column=Column("course_code", String, unique=True))



class CategoryRead(CategoryBase):
    id: int


class CategoryUpdate(SQLModel): 
    name: Optional[str] = None


