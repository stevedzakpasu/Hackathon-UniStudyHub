from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.api.deps import get_current_active_superuser
from app.core.deps import get_session
from app.crud.crud_university import university
from app.schemas.university import UniversityUpdate, UniversityRead, UniversityCreate

router = APIRouter()

@router.get("/universities", response_model=List[UniversityRead], dependencies=[Depends(get_current_active_superuser)])
def get_universities(
    *, 
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = 100
    ):
    universities = university.get_multiple(session=session, offset=offset, limit=limit)
    return universities



@router.post("/universities", response_model=UniversityCreate, dependencies=[Depends(get_current_active_superuser)])
def create_university(
    *,
    session: Session = Depends(get_session),
    university_in: UniversityCreate,

    ):
    db_university= university.get_by_name(session=session, name=university_in.name)
    
    if db_university:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="university with this university name already exists"
        )
    

    new_university = university.create(session=session, obj_in=university_in)
    return new_university




@router.get("/universities/{id}", response_model=UniversityRead, dependencies=[Depends(get_current_active_superuser)])
def get_university(
    *,
    session: Session = Depends(get_session),
    id: int
    ):
    db_university = university.get_by_id(session=session, id=id)
    if not db_university:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="University not found"
        )
    return db_university


@router.put("/universities", response_model=UniversityRead, dependencies=[Depends(get_current_active_superuser)])
def update_university(
    *,
    session: Session = Depends(get_session),
    university_in: UniversityUpdate,
    university_id: str
    ):
    updated_university = university.update(session=session, university_id=university_id, obj_in=university_in)
    if not updated_university:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="university not found"
        )
    return updated_university



@router.delete("/universities", dependencies=[Depends(get_current_active_superuser)])
def delete_university(
    *,
    session: Session = Depends(get_session),
    id: int
    ):
    deleted_university = university.remove(session=session, id=id)
    if not deleted_university:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="university not found"
        )
    return {"success": "university deleted successfully"}