from datetime import datetime
from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Relationship, SQLModel, Field, Column, String
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from app.models.useruniversity import UserUniversity
if TYPE_CHECKING:
    from app.models.user import User


class UniversityBase(SQLModel):
    name : str = Field(
        index=True, sa_column=Column("name", String, unique=True))
    users: List["User"] = Relationship(back_populates="universities", link_model=UserUniversity)

class UniversityCreate(SQLModel):
    name : str = Field(
        index=True, sa_column=Column("course_code", String, unique=True))



class UniversityRead(UniversityBase):
    id: int


class UniversityUpdate(SQLModel): 
    name: Optional[str] = None


