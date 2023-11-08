from typing import Optional
from sqlmodel import Field

from app.schemas.comment import CommentBase

class Comment(CommentBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)