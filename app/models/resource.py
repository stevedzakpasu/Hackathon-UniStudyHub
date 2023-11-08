from typing import Optional
from sqlmodel import Field

from app.schemas.resource import ResourceBase

class Resource(ResourceBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)