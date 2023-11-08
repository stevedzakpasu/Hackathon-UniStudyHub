from typing import Optional
from sqlmodel import Field

from app.schemas.report import ReportBase

class Report(ReportBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)