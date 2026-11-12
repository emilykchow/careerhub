from app.models.sa.base import Base
from sqlalchemy import Array, Boolean, Column, Integer, String


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    auth0_id = Column(
        String,
        unique=True,
        nullable=False,
    )
    name = Column(String, nullable=False)
    email = Column(
        String,
        unique=True,
        nullable=False,
    )
    email_verified = Column(Boolean, nullable=False)
    password = Column(String, nullable=False)
    picture = Column(String, nullable=True)
    target_job_titles = Column(
        Array(String),
        nullable=True,
        default=list,
    )
