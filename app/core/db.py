from sqlmodel import create_engine
from app.core.settings import settings

# this is for the postgres db
# engine = create_engine(settings.DB_URL, echo=False)


engine = create_engine(settings.DB_URL, echo=False)


