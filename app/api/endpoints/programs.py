from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.api.deps import get_current_active_superuser
from app.core.deps import get_session
from app.crud.crud_program import program
from app.schemas.program import ProgramUpdate, ProgramRead, ProgramCreate

router = APIRouter()

@router.get("/programs", response_model=List[ProgramRead], dependencies=[Depends(get_current_active_superuser)])
def get_programs(
    *, 
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = 100
    ):
    programs = program.get_multiple(session=session, offset=offset, limit=limit)
    return programs



@router.post("/programs", response_model=ProgramCreate, dependencies=[Depends(get_current_active_superuser)])
def create_program(
    *,
    session: Session = Depends(get_session),
    program_in: ProgramCreate,

    ):
    db_program= program.get_by_name(session=session, name=program_in.name)
    
    if db_program:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Program with this Program name already exists"
        )
    

    new_program = program.create(session=session, obj_in=program_in)
    return new_program




@router.get("/programs/{name}", response_model=ProgramRead, dependencies=[Depends(get_current_active_superuser)])
def get_program(
    *,
    session: Session = Depends(get_session),
    name: str
    ):
    db_program = program.get_by_name(session=session, name=name)
    if not db_program:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Program not found"
        )
    return db_program


@router.put("/programs", response_model=ProgramRead, dependencies=[Depends(get_current_active_superuser)])
def update_program(
    *,
    session: Session = Depends(get_session),
    program_in: ProgramUpdate,
    id: int
    ):
    updated_program = program.update(session=session, id=id, obj_in=program_in)
    if not updated_program:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Program not found"
        )
    return updated_program



@router.delete("/programs", dependencies=[Depends(get_current_active_superuser)])
def delete_program(
    *,
    session: Session = Depends(get_session),
    name: str
    ):
    deleted_program = program.remove(session=session, name=name)
    if not deleted_program:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Program not found"
        )
    return {"success": "Program deleted successfully"}