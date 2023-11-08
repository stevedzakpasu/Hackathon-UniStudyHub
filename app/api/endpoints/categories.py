from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.api.deps import get_current_active_superuser
from app.core.deps import get_session
from app.crud.crud_category import category
from app.schemas.category import CategoryUpdate, CategoryRead, CategoryCreate

router = APIRouter()

@router.get("/categories", response_model=List[CategoryRead], dependencies=[Depends(get_current_active_superuser)])
def get_categories(
    *, 
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = 100
    ):
    categories = category.get_multiple(session=session, offset=offset, limit=limit)
    return categories



@router.post("/categories", response_model=CategoryCreate, dependencies=[Depends(get_current_active_superuser)])
def create_category(
    *,
    session: Session = Depends(get_session),
    category_in: CategoryCreate,

    ):
    db_category= category.get_by_name(session=session, name=category_in.name)
    
    if db_category:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category with this Category name already exists"
        )
    

    new_category = category.create(session=session, obj_in=category_in)
    return new_category




@router.get("/categories/{name}", response_model=CategoryRead, dependencies=[Depends(get_current_active_superuser)])
def get_category(
    *,
    session: Session = Depends(get_session),
    name: str
    ):
    db_category = category.get_by_name(session=session, name=name)
    if not db_category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    return db_category


@router.put("/categories", response_model=CategoryRead, dependencies=[Depends(get_current_active_superuser)])
def update_category(
    *,
    session: Session = Depends(get_session),
    category_in: CategoryUpdate,
    id: int
    ):
    updated_category = category.update(session=session, id=id, obj_in=category_in)
    if not updated_category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    return updated_category



@router.delete("/categories", dependencies=[Depends(get_current_active_superuser)])
def delete_category(
    *,
    session: Session = Depends(get_session),
    name: str
    ):
    deleted_category = category.remove(session=session, name=name)
    if not deleted_category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    return {"success": "Category deleted successfully"}