from fastapi import HTTPException
from sqlmodel import Session, col, select
from app.models.course import Course
from app.schemas.course import CourseCreate, CourseUpdate
from app.crud.base import CRUDBase


class CRUDCourse(CRUDBase[Course, CourseCreate, CourseUpdate]):



    def get_by_id(self, *, session: Session, id: int) -> Course:
        return session.exec(select(Course).where(col(Course.id) == id)).first()  

    def get_by_name(self, *, session: Session, name: str) -> Course:
        return session.exec(select(Course).where(col(Course.name) == name)).first()  


    


    
    def create(self, *, session: Session, obj_in: CourseCreate) -> Course:
    

        db_obj = Course(
            name= obj_in.name,
            category_id=obj_in.category_id,
            university_id=obj_in.university_id

        )

        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj



    def update(self, *, session: Session, id: int, obj_in: CourseUpdate) -> Course:
        db_obj = session.exec(select(Course).where(col(Course.id) == id)).first()
        if db_obj: 
            obj_data = obj_in.dict(exclude_unset=True)
            for key, value in obj_data.items():
                setattr(db_obj, key, value)
            session.add(db_obj)
            session.commit()
            session.refresh(db_obj)
        return db_obj

    def remove(self, *, session: Session, id: int) -> Course:
        db_obj = session.exec(select(Course).where(col(Course.id) == id)).first()
        if not db_obj:
            raise HTTPException(status_code=404, detail="Course not found")
        session.delete(db_obj)
        session.commit()
            
        return db_obj

    



course = CRUDCourse(Course)
