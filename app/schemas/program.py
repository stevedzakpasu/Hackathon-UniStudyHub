from datetime import datetime
from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Relationship, SQLModel, Field, Column, String
from sqlalchemy import DateTime
from sqlalchemy.sql import func
# from app.models.userprogram import UserProgram
if TYPE_CHECKING:
    from app.models.user import User


class ProgramBase(SQLModel):
    name : str = Field(
        index=True, sa_column=Column("name", String, unique=True))
    users: List["User"] = Relationship(back_populates="program")

class ProgramCreate(SQLModel):
    name : str = Field(
        index=True, sa_column=Column("course_code", String, unique=True))



class ProgramRead(ProgramBase):
    id: int


class ProgramUpdate(SQLModel): 
    name: Optional[str] = None


