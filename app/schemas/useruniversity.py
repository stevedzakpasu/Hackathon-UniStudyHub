from sqlmodel import SQLModel, Field


class UserUniversityBase(SQLModel):
    user_id: str = Field(foreign_key="user.id", primary_key=True)
    university_name: str = Field(foreign_key="university.name", primary_key=True)

