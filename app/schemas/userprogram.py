from sqlmodel import SQLModel, Field


class UserProgramBase(SQLModel):
    user_id: str = Field(foreign_key="user.id", primary_key=True)
    program_name: str = Field(foreign_key="program.name", primary_key=True)

