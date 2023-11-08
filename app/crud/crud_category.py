from fastapi import HTTPException
from sqlmodel import Session, col, select
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate
from app.crud.base import CRUDBase


class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):



    def get_by_id(self, *, session: Session, id: int) -> Category:
        return session.exec(select(Category).where(col(Category.id) == id)).first()  

    def get_by_name(self, *, session: Session, name: str) -> Category:
        return session.exec(select(Category).where(col(Category.name) == name)).first()  


    


    
    def create(self, *, session: Session, obj_in: CategoryCreate) -> Category:
    

        db_obj = Category(
            name= obj_in.name,

        )

        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj



    def update(self, *, session: Session, id: int, obj_in: CategoryUpdate) -> Category:
        db_obj = session.exec(select(Category).where(col(Category.id) == id)).first()
        if db_obj: 
            obj_data = obj_in.dict(exclude_unset=True)
            for key, value in obj_data.items():
                setattr(db_obj, key, value)
            session.add(db_obj)
            session.commit()
            session.refresh(db_obj)
        return db_obj

    def remove(self, *, session: Session, id: int) -> Category:
        db_obj = session.exec(select(Category).where(col(Category.id) == id)).first()
        if not db_obj:
            raise HTTPException(status_code=404, detail="Category not found")
        session.delete(db_obj)
        session.commit()
            
        return db_obj

    



category = CRUDCategory(Category)
