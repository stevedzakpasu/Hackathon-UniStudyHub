from datetime import datetime
from typing import TYPE_CHECKING, List, Optional
from pydantic import EmailStr
from sqlmodel import Relationship, SQLModel, Field, Column, String
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from app.models.university import University
from app.models.program import Program
if TYPE_CHECKING:
    from app.models.resource import Resource
class UserBase(SQLModel):
    username: str
    email: EmailStr = Field(
        index=True, sa_column=Column("email", String, unique=True)) 
    verification_code: Optional[str] = None
    code_expiration_time: Optional[datetime] = None
    is_superuser: Optional[bool] = Field(default=False)
    is_active: Optional[bool] = Field(default=True)
    is_verified : Optional[bool] = Field(default=False)
    created_at: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now()))
    updated_at: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), onupdate=func.now())
    )
    university_id : Optional[int] = Field(default=None, foreign_key="university.id")
    university: University = Relationship(back_populates="users")
    program_id : Optional[int] = Field(default=None, foreign_key="program.id")
    program: Program = Relationship(back_populates="users")
    resources: List["Resource"] = Relationship(back_populates="users")
    


class UserAdminCreate(SQLModel):
    username: str
    email: EmailStr = Field(
        index=True, sa_column=Column("email", String, unique=True)) 
    password: str
    is_superuser: Optional[bool] = Field(default=False)
    is_active: Optional[bool] = Field(default=True)
    is_verified : Optional[bool] = Field(default=False)
    university_id : Optional[int] = Field(default=None,foreign_key="university.id")
    program_id : Optional[int] = Field(default=None, foreign_key="program.id")


class UserCreate(SQLModel):
    username: str
    email: EmailStr
    password: str
    university_id : Optional[int] = Field(default=None,foreign_key="university.id")
    program_id : Optional[int] = Field(default=None, foreign_key="program.id")

class UserCreateReturn(SQLModel):
    id: int
    username: str
    email: EmailStr
    is_superuser: bool
    is_active: bool
    is_verified : bool
    university_id: Optional[int]
    program_id : Optional[int]

class UserRead(UserBase):
    id: int


class UserAdminUpdate(SQLModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    is_superuser: Optional[bool] = False
    is_active: Optional[bool] = None
    is_verified: Optional[bool] = None
    university_id : Optional[int] = None
    program_id : Optional[int] = None

class UserUpdate(SQLModel):
    pass

