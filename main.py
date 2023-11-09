from fastapi import FastAPI
from app.core.deps import create_superuser
from app.core.settings import settings
from app.api.api import api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=settings.PROJECT_NAME)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    create_superuser()

    
app.include_router(api_router, prefix="/api")