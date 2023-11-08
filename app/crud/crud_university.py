from fastapi import HTTPException
from sqlmodel import Session, col, select
from app.models.university import University
from app.schemas.university import UniversityCreate,UniversityRead, UniversityUpdate
from app.crud.base import CRUDBase


class CRUDUniversity(CRUDBase[University, UniversityCreate, UniversityUpdate]):



    def get_by_id(self, *, session: Session, id: int) -> University:
        return session.exec(select(University).where(col(University.id) == id)).first()  

    def get_by_name(self, *, session: Session, name: str) -> University:
        return session.exec(select(University).where(col(University.name) == name)).first()  


    


    
    def create(self, *, session: Session, obj_in: UniversityCreate) -> University:
    

        db_obj = University(
            name= obj_in.name,

        )

        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj



    def update(self, *, session: Session, id: int, obj_in: UniversityUpdate) -> University:
        db_obj = session.exec(select(University).where(col(University.id) == id)).first()
        if db_obj: 
            obj_data = obj_in.dict(exclude_unset=True)
            for key, value in obj_data.items():
                setattr(db_obj, key, value)
            session.add(db_obj)
            session.commit()
            session.refresh(db_obj)
        return db_obj

    def remove(self, *, session: Session, id: int) -> University:
        db_obj = session.exec(select(University).where(col(University.id) == id)).first()
        if not db_obj:
            raise HTTPException(status_code=404, detail="University not found")
        session.delete(db_obj)
        session.commit()
            
        return db_obj

    



university = CRUDUniversity(University)
