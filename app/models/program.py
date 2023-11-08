from typing import Optional
from sqlmodel import Field

from app.schemas.program import ProgramBase

class Program(ProgramBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

