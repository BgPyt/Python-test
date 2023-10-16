import pytest
from sqlalchemy.orm import sessionmaker, Session
from fastapi.testclient import TestClient
from src.config import DB_USER, DB_HOST, DB_PASS, DB_PORT, DB_NAME_TEST
from sqlalchemy import create_engine
from src.database import get_session, Base
from src.main import app

DATABASE_URL_TEST = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME_TEST}"

engine_test = create_engine(DATABASE_URL_TEST)
session_maker = sessionmaker(bind=engine_test, autocommit=False, autoflush=False)


def override_get_session() -> Session:
    with session_maker() as session:
        yield session


app.dependency_overrides[get_session] = override_get_session


@pytest.fixture(autouse=True, scope='session')
def prepare_database():
    Base.metadata.create_all(bind=engine_test)
    yield
    Base.metadata.drop_all(bind=engine_test)


client = TestClient(app)

