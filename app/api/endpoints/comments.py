from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.api.deps import get_current_active_superuser, get_current_active_user
from app.core.deps import get_session
from app.crud.crud_comment import comment
from app.schemas.comment import CommentUpdate, CommentRead, CommentCreate

router = APIRouter()

@router.get("/comments", response_model=List[CommentRead], dependencies=[Depends(get_current_active_user)])
def get_comments(
    *, 
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = 100
    ):
    comments = comment.get_multiple(session=session, offset=offset, limit=limit)
    return comments



@router.post("/comments", response_model=CommentCreate, dependencies=[Depends(get_current_active_user)])
def create_comment(
    *,
    session: Session = Depends(get_session),
    comment_in: CommentCreate,

    ):

    

    new_comment = comment.create(session=session, obj_in=comment_in)
    return new_comment




@router.get("/comments/{name}", response_model=CommentRead, dependencies=[Depends(get_current_active_user)])
def get_comment(
    *,
    session: Session = Depends(get_session),
    name: str
    ):
    db_comment = comment.get_by_name(session=session, name=name)
    if not db_comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comment not found"
        )
    return db_comment


@router.put("/comments", response_model=CommentRead, dependencies=[Depends(get_current_active_user)])
def update_comment(
    *,
    session: Session = Depends(get_session),
    comment_in: CommentUpdate,
    id: int
    ):
    updated_comment = comment.update(session=session, id=id, obj_in=comment_in)
    if not updated_comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comment not found"
        )
    return updated_comment



@router.delete("/comments", dependencies=[Depends(get_current_active_user)])
def delete_comment(
    *,
    session: Session = Depends(get_session),
    name: str
    ):
    deleted_comment = comment.remove(session=session, name=name)
    if not deleted_comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comment not found"
        )
    return {"success": "Comment deleted successfully"}