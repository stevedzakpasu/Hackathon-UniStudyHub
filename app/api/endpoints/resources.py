from typing import List
from fastapi import UploadFile, File
from mega import Mega
import tempfile
import os
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.api.deps import get_current_active_superuser, get_current_active_user
from app.core.deps import get_session
from app.crud.crud_resource import resource
from app.schemas.resource import ResourceUpdate, ResourceRead, ResourceCreate,ResourceReadWIthLikes
import shutil
import os

router = APIRouter()

@router.get("/resources", response_model=List[ResourceRead], dependencies=[Depends(get_current_active_user)])
def get_resources(
    *, 
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = 100
    ):
    resources = resource.get_multiple(session=session, offset=offset, limit=limit)
    return resources



# Assuming `resource_in` contains the URL field, modify the function signature accordingly if needed.
@router.post("/upload_resource", dependencies=[Depends(get_current_active_user)])
async def upload_resource(
    *,
    file: UploadFile = File(...),  # Include UploadFile parameter for file upload
):
    # Save the uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(file.file.read())
        temp_file_path = temp_file.name
    
    newFile = file.filename #+".pdf"
    # os.rename(temp_file_path, newFile)
    shutil.copy(src=temp_file_path,dst=newFile)

    # Initialize Mega client
    mega = Mega()
    m = mega.login('unistudyhub@gmail.com', 'UniStudyHub@2023')

    # Upload the file to Mega
    mega_file = m.upload(newFile)

    os.remove(newFile)
    # Get the Mega download link
    mega_link = mega.get_upload_link(mega_file)



# Assuming `resource_in` contains the URL field, modify the function signature accordingly if needed.
@router.post("/upload_resource", dependencies=[Depends(get_current_active_user)])
async def upload_resource(
    *,
    url: str ,  # Include UploadFile parameter for file upload
):


    # Initialize Mega client
    mega = Mega()
    m = mega.login('unistudyhub@gmail.com', 'UniStudyHub@2023')

    m.download_url(url)




    return True

@router.post("/resources", dependencies=[Depends(get_current_active_user)])
async def create_resource(
    *,
    session: Session = Depends(get_session),
    resource_in: ResourceCreate,  # Include UploadFile parameter for file upload
):

    new_resource = resource.create(session=session, obj_in=resource_in)

    return new_resource



@router.get("/resources/{id}", response_model=ResourceRead, dependencies=[Depends(get_current_active_superuser)])
def get_resource(
    *,
    session: Session = Depends(get_session),
    id: str
    ):
    db_resource = resource.get_by_id(session=session, id=id)
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



@router.delete("/resources", dependencies=[Depends(get_current_active_user)])
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