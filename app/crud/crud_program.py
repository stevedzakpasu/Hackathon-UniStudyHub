from fastapi import HTTPException
from sqlmodel import Session, col, select
from app.models.program import Program
from app.schemas.program import ProgramCreate, ProgramUpdate
from app.crud.base import CRUDBase


class CRUDProgram(CRUDBase[Program, ProgramCreate, ProgramUpdate]):



    def get_by_id(self, *, session: Session, id: int) -> Program:
        return session.exec(select(Program).where(col(Program.id) == id)).first()  

    def get_by_name(self, *, session: Session, name: str) -> Program:
        return session.exec(select(Program).where(col(Program.name) == name)).first()  


    


    
    def create(self, *, session: Session, obj_in: ProgramCreate) -> Program:
    

        db_obj = Program(
            name= obj_in.name,

        )

        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj



    def update(self, *, session: Session, id: int, obj_in: ProgramUpdate) -> Program:
        db_obj = session.exec(select(Program).where(col(Program.id) == id)).first()
        if db_obj: 
            obj_data = obj_in.dict(exclude_unset=True)
            for key, value in obj_data.items():
                setattr(db_obj, key, value)
            session.add(db_obj)
            session.commit()
            session.refresh(db_obj)
        return db_obj

    def remove(self, *, session: Session, id: int) -> Program:
        db_obj = session.exec(select(Program).where(col(Program.id) == id)).first()
        if not db_obj:
            raise HTTPException(status_code=404, detail="Program not found")
        session.delete(db_obj)
        session.commit()
            
        return db_obj

    



program = CRUDProgram(Program)
