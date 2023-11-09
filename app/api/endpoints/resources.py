from typing import List
from fastapi import UploadFile, File
from mega import Mega
import tempfile
import os
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.api.deps import get_current_active_superuser
from app.core.deps import get_session
from app.crud.crud_resource import resource
from app.schemas.resource import ResourceUpdate, ResourceRead, ResourceCreate

router = APIRouter()

@router.get("/resources", response_model=List[ResourceRead], dependencies=[Depends(get_current_active_superuser)])
def get_resources(
    *, 
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = 100
    ):
    resources = resource.get_multiple(session=session, offset=offset, limit=limit)
    return resources



# Assuming `resource_in` contains the URL field, modify the function signature accordingly if needed.
@router.post("/resources", response_model=ResourceCreate, dependencies=[Depends(get_current_active_superuser)])
def create_resource(
    *,
    session: Session = Depends(get_session),
    resource_in: ResourceCreate,
    uploaded_file: UploadFile = File(...),  # Include UploadFile parameter for file upload
):
    # Save the uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.file.read())
        temp_file_path = temp_file.name

    # Initialize Mega client
    mega = Mega()
    m = mega.login('unistudyhub@gmail.com', 'UniStudyHub@2023')

    # Upload the file to Mega
    mega_file = m.upload(temp_file_path)

    # Get the Mega download link
    mega_link = mega.get_upload_link(mega_file)

    # Clean up the temporary file
    os.remove(temp_file_path)

    # Assign the Mega download link to the URL field in resource_in
    resource_in.url = mega_link


    # Create the resource in your database using resource.create() function (assuming it's defined somewhere)
    new_resource = resource.create(session=session, obj_in=resource_in)

    return new_resource



@router.get("/resources/{id}", response_model=ResourceRead, dependencies=[Depends(get_current_active_superuser)])
def get_resource(
    *,
    session: Session = Depends(get_session),
    id: str
    ):
    db_resource = resource.get_by_resource_code(session=session, id=id)
    if not db_resource:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="resource not found"
        )
    return db_resource


@router.put("/resources", response_model=ResourceRead, dependencies=[Depends(get_current_active_superuser)])
def update_resource(
    *,
    session: Session = Depends(get_session),
    resource_in: ResourceUpdate,
    id: int
    ):
    updated_resource = resource.update(session=session, id=id, obj_in=resource_in)
    if not updated_resource:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="resource not found"
        )
    return updated_resource



@router.delete("/resources", dependencies=[Depends(get_current_active_superuser)])
def delete_resource(
    *,
    session: Session = Depends(get_session),
    id: int
    ):
    deleted_resource = resource.remove(session=session, id=id)
    if not deleted_resource:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="resource not found"
        )
    return {"success": "resource deleted successfully"}