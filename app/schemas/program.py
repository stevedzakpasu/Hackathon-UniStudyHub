from sqlmodel import Relationship, SQLModel
from typing import List, Optional
from app.models.user import User
class ProgramBase(SQLModel):
    name: str
    users: List["User"] = Relationship(back_populates=("program"))

class ProgramCreate(ProgramBase):
    pass 
   
class ProgramCreateReturn(ProgramBase):
    id: int 

class ProgramRead(ProgramBase):
    id:int 

class ProgramAdminUpdate(SQLModel):
    name: Optional[str] = None 
 

class ProgramUpdate(SQLModel):
    pass
