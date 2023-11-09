from sqlmodel import Session
from app.core.db import engine
from app.core.security import get_hashed_password
from app.core.settings import settings
from app.crud.crud_user import user
from app.crud.crud_university import university
from app.models.user import User
from app.models.university import University


def get_session():
    with Session(engine) as session:
        yield session


def create_superuser():
    with Session(engine) as session:
        super_user = user.get_by_email(
            session=session, email=settings.SUPERUSER_EMAIL)
        if not super_user:
            new_user = User(
                username=settings.SUPERUSER_USERNAME,
                email=settings.SUPERUSER_EMAIL,
                hashed_password=get_hashed_password(
                    settings.SUPERUSER_PASSWORD),
                is_superuser=settings.SUPERUSER,
                is_verified=settings.VERIFIED
            )
            session.add(new_user)
            session.commit()


def populate_database():
    
    universityList = [
        "University of Ghana",
        "Kwame Nkrumah University of Science and Technology",
        "University of Cape Coast",
        "University of Education, Winneba",
        "All Nations University",
        "University of Mines and Technology",
        "University of Professional Studies",
        "University for Development Studies",
        "Ashesi University",

    ]

    for universityName in universityList:
        with Session(engine) as session:
            theUni = university.get_by_name(session=session, name=universityName)
            if not theUni:
                new_uni = University(name=universityName)
                session.add(new_uni)
                session.commit()














