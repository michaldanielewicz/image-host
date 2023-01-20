import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import config
from app.database import Base, get_db
from app.main import app


SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{config.USER}:{config.PASSWORD}@app_db/{config.DB}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def test_client():
    return TestClient(app)
