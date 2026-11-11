from app.models.sa.base import Base
from sqlalchemy import Boolean, Column, Integer, String


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    auth0_id = Column(String, unique=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    nick_name = Column(String, nullable=True)
    picture = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    email_verified = Column(Boolean, nullable=False)
