from typing import Optional
from sqlmodel import Field

from app.schemas.category import CategoryBase

class Category(CategoryBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

