from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.api.deps import get_current_active_superuser
from app.core.deps import get_session
from app.crud.crud_like import like
from app.schemas.like import LikeUpdate, LikeRead, LikeCreate

router = APIRouter()

@router.get("/likes", response_model=List[LikeRead], dependencies=[Depends(get_current_active_superuser)])
def get_likes(
    *, 
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = 100
    ):
    likes = like.get_multiple(session=session, offset=offset, limit=limit)
    return likes



@router.post("/likes", response_model=LikeCreate, dependencies=[Depends(get_current_active_superuser)])
def create_like(
    *,
    session: Session = Depends(get_session),
    like_in: LikeCreate,

    ):

    

    new_like = like.create(session=session, obj_in=like_in)
    return new_like




@router.get("/likes/{name}", response_model=LikeRead, dependencies=[Depends(get_current_active_superuser)])
def get_like(
    *,
    session: Session = Depends(get_session),
    name: str
    ):
    db_like = like.get_by_name(session=session, name=name)
    if not db_like:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="like not found"
        )
    return db_like


@router.put("/likes", response_model=LikeRead, dependencies=[Depends(get_current_active_superuser)])
def update_like(
    *,
    session: Session = Depends(get_session),
    like_in: LikeUpdate,
    id: int
    ):
    updated_like = like.update(session=session, id=id, obj_in=like_in)
    if not updated_like:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="like not found"
        )
    return updated_like



@router.delete("/likes", dependencies=[Depends(get_current_active_superuser)])
def delete_like(
    *,
    session: Session = Depends(get_session),
    name: str
    ):
    deleted_like = like.remove(session=session, name=name)
    if not deleted_like:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="like not found"
        )
    return {"success": "like deleted successfully"}