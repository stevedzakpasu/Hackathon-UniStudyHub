from datetime import datetime
from typing import TYPE_CHECKING, Optional
from pydantic import EmailStr
from sqlmodel import Relationship, SQLModel, Field, Column, String
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from app.models.useruniversity import UserUniversity

from app.models.university import University

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
    university: University = Relationship(back_populates="users", link_model=UserUniversity)
    


class UserAdminCreate(SQLModel):
    username: str
    email: EmailStr = Field(
        index=True, sa_column=Column("email", String, unique=True)) 
    password: str
    is_superuser: Optional[bool] = Field(default=False)
    is_active: Optional[bool] = Field(default=True)
    is_verified : Optional[bool] = Field(default=False)


class UserCreate(SQLModel):
    username: str
    email: EmailStr
    password: str


class UserCreateReturn(SQLModel):
    id: int
    username: str
    email: EmailStr
    is_superuser: bool
    is_active: bool
    is_verified : bool


class UserRead(UserBase):
    id: int


class UserAdminUpdate(SQLModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    is_superuser: Optional[bool] = False
    is_active: Optional[bool] = None
    is_verified: Optional[bool] = None

class UserUpdate(SQLModel):
    pass

