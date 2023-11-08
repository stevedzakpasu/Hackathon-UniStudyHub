from fastapi import HTTPException
from sqlmodel import Session, col, select
from app.models.comment import Comment
from app.schemas.comment import CommentCreate, CommentUpdate
from app.crud.base import CRUDBase


class CRUDComment(CRUDBase[Comment, CommentCreate, CommentUpdate]):



    def get_by_id(self, *, session: Session, id: int) -> Comment:
        return session.exec(select(Comment).where(col(Comment.id) == id)).first()  


    
    def create(self, *, session: Session, obj_in: CommentCreate) -> Comment:
    

        db_obj = Comment(
            text= obj_in.text,
            resource_id=obj_in.resource_id

        )

        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj



    def update(self, *, session: Session, id: int, obj_in: CommentUpdate) -> Comment:
        db_obj = session.exec(select(Comment).where(col(Comment.id) == id)).first()
        if db_obj: 
            obj_data = obj_in.dict(exclude_unset=True)
            for key, value in obj_data.items():
                setattr(db_obj, key, value)
            session.add(db_obj)
            session.commit()
            session.refresh(db_obj)
        return db_obj

    def remove(self, *, session: Session, id: int) -> Comment:
        db_obj = session.exec(select(Comment).where(col(Comment.id) == id)).first()
        if not db_obj:
            raise HTTPException(status_code=404, detail="Comment not found")
        session.delete(db_obj)
        session.commit()
            
        return db_obj

    



comment = CRUDComment(Comment)
