from fastapi import HTTPException
from sqlmodel import Session, col, select
from app.models.report import Report
from app.schemas.report import ReportCreate, ReportUpdate
from app.crud.base import CRUDBase


class CRUDReport(CRUDBase[Report, ReportCreate, ReportUpdate]):



    def get_by_id(self, *, session: Session, id: int) -> Report:
        return session.exec(select(Report).where(col(Report.id) == id)).first()  


    
    def create(self, *, session: Session, obj_in: ReportCreate) -> Report:
    

        db_obj = Report(
          
            resource_id=obj_in.resource_id

        )

        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj



    def update(self, *, session: Session, id: int, obj_in: ReportUpdate) -> Report:
        db_obj = session.exec(select(Report).where(col(Report.id) == id)).first()
        if db_obj: 
            obj_data = obj_in.dict(exclude_unset=True)
            for key, value in obj_data.items():
                setattr(db_obj, key, value)
            session.add(db_obj)
            session.commit()
            session.refresh(db_obj)
        return db_obj

    def remove(self, *, session: Session, id: int) -> Report:
        db_obj = session.exec(select(Report).where(col(Report.id) == id)).first()
        if not db_obj:
            raise HTTPException(status_code=404, detail="Report not found")
        session.delete(db_obj)
        session.commit()
            
        return db_obj

    



report = CRUDReport(Report)
