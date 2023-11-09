from fastapi import HTTPException
from sqlmodel import Session, col, select
from app.models.resource import Resource
from app.schemas.resource import ResourceCreate, ResourceUpdate
from app.crud.base import CRUDBase


class CRUDResource(CRUDBase[Resource, ResourceCreate, ResourceUpdate]):



    def get_by_id(self, *, session: Session, id: int) -> Resource:
        return session.exec(select(Resource).where(col(Resource.id) == id)).first()  

    def get_by_description(self, *, session: Session, description: str) -> Resource:
        return session.exec(select(Resource).where(col(Resource.description) == description)).first()  


    
    def create(self, *, session: Session, obj_in: ResourceCreate) -> Resource:
    

        db_obj = Resource(
            description= obj_in.description,
            user_id=obj_in.user_id,
            category_id=obj_in.category_id,
            course_id=obj_in.course_id,
            url=obj_in.url,
            title=obj_in.title

        )

        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj



    def update(self, *, session: Session, id: int, obj_in: ResourceUpdate) -> Resource:
        db_obj = session.exec(select(Resource).where(col(Resource.id) == id)).first()
        if db_obj: 
            obj_data = obj_in.dict(exclude_unset=True)
            for key, value in obj_data.items():
                setattr(db_obj, key, value)
            session.add(db_obj)
            session.commit()
            session.refresh(db_obj)
        return db_obj

    def remove(self, *, session: Session, id: int) -> Resource:
        db_obj = session.exec(select(Resource).where(col(Resource.id) == id)).first()
        if not db_obj:
            raise HTTPException(status_code=404, detail="Resource not found")
        session.delete(db_obj)
        session.commit()
            
        return db_obj

    



resource = CRUDResource(Resource)
