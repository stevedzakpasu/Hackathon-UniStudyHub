from typing import Optional
from sqlmodel import Field

from app.schemas.university import UniversityBase

class University(UniversityBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

