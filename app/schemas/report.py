from datetime import datetime
from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Relationship, SQLModel, Field, Column, String
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from app.models.resource import Resource




class ReportBase(SQLModel):
    resource_id : int = Field(foreign_key="resource.id", default=None)
    created_at: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now()))
    resource: Resource = Relationship(back_populates="report")

class ReportCreate(ReportBase):
    pass


class ReportRead(ReportBase):
    id: int


class ReportUpdate(SQLModel): 
    resource_id: Optional[int] = None



