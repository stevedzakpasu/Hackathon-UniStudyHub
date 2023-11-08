from sqlmodel import create_engine
from app.core.settings import settings

# this is for the postgres db
# engine = create_engine(settings.DB_URL, echo=False)


sqlite_url = "sqlite:///database.db"
engine = create_engine(sqlite_url, echo=True, connect_args={"check_same_thread":False})


