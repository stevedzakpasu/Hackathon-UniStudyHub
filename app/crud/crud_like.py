from fastapi import HTTPException
from sqlmodel import Session, col, select
from app.models.like import Like
from app.schemas.like import LikeCreate, LikeUpdate
from app.crud.base import CRUDBase


class CRUDLike(CRUDBase[Like, LikeCreate, LikeUpdate]):



    def get_by_id(self, *, session: Session, id: int) -> Like:
        return session.exec(select(Like).where(col(Like.id) == id)).first()  


    
    def create(self, *, session: Session, obj_in: LikeCreate) -> Like:
    

        db_obj = Like(
          
            resource_id=obj_in.resource_id

        )

        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj



    def update(self, *, session: Session, id: int, obj_in: LikeUpdate) -> Like:
        db_obj = session.exec(select(Like).where(col(Like.id) == id)).first()
        if db_obj: 
            obj_data = obj_in.dict(exclude_unset=True)
            for key, value in obj_data.items():
                setattr(db_obj, key, value)
            session.add(db_obj)
            session.commit()
            session.refresh(db_obj)
        return db_obj

    def remove(self, *, session: Session, id: int) -> Like:
        db_obj = session.exec(select(Like).where(col(Like.id) == id)).first()
        if not db_obj:
            raise HTTPException(status_code=404, detail="Like not found")
        session.delete(db_obj)
        session.commit()
            
        return db_obj

    



like = CRUDLike(Like)
