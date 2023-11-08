from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.api.deps import get_current_active_superuser
from app.core.deps import get_session
from app.crud.crud_report import report
from app.schemas.report import ReportCreate, ReportRead, ReportUpdate

router = APIRouter()

@router.get("/reports", response_model=List[ReportRead], dependencies=[Depends(get_current_active_superuser)])
def get_reports(
    *, 
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = 100
    ):
    reports = report.get_multiple(session=session, offset=offset, limit=limit)
    return reports



@router.post("/reports", response_model=ReportUpdate, dependencies=[Depends(get_current_active_superuser)])
def create_report(
    *,
    session: Session = Depends(get_session),
    like_in: ReportUpdate,

    ):

    

    new_report = report.create(session=session, obj_in=like_in)
    return new_report




@router.get("/reports/{name}", response_model=ReportRead, dependencies=[Depends(get_current_active_superuser)])
def get_report(
    *,
    session: Session = Depends(get_session),
    name: str
    ):
    db_report = report.get_by_name(session=session, name=name)
    if not db_report:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Report not found"
        )
    return db_report


@router.put("/reports", response_model=ReportRead, dependencies=[Depends(get_current_active_superuser)])
def update_report(
    *,
    session: Session = Depends(get_session),
    like_in: ReportCreate,
    id: int
    ):
    updated_report = report.update(session=session, id=id, obj_in=like_in)
    if not updated_report:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Report not found"
        )
    return updated_report



@router.delete("/reports", dependencies=[Depends(get_current_active_superuser)])
def delete_report(
    *,
    session: Session = Depends(get_session),
    name: str
    ):
    deleted_report = report.remove(session=session, name=name)
    if not deleted_report:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Report not found"
        )
    return {"success": "Report deleted successfully"}