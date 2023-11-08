from typing import Optional
from sqlmodel import Field

from app.schemas.like import LikeBase

class Like(LikeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)