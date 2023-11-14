from datetime import datetime
from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Relationship, SQLModel, Field, Column, String
from sqlalchemy import DateTime
from sqlalchemy.sql import func

class CourseBase(SQLModel):
    name : str = Field(
        index=True, sa_column=Column("name", String, unique=True))
    university_id : int = Field(foreign_key="university.id", default=None)
  
class CourseCreate(CourseBase):
    pass

class CourseRead(CourseBase):
    id: int

class CourseUpdate(SQLModel): 
    name: Optional[str] = None
    university_id : Optional[int] = None
