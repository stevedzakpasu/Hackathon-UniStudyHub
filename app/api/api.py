from fastapi import APIRouter
from app.api.endpoints import users, login, verification, universities, programs, categories, courses, resources,comments,likes,reports


api_router = APIRouter()


api_router.include_router(users.router, tags=["Users"])
api_router.include_router(login.router, tags=["Login"])
api_router.include_router(verification.router, tags=["Verification"])
api_router.include_router(universities.router, tags=["Universities"])
api_router.include_router(programs.router, tags=["Programs"])
api_router.include_router(categories.router, tags=["Categories"])
api_router.include_router(courses.router, tags=["Courses"])
api_router.include_router(resources.router, tags=["Resources"])
api_router.include_router(comments.router, tags=["Comments"])
api_router.include_router(likes.router, tags=["Likes"])
api_router.include_router(reports.router, tags=["Reports"])


