from app.constants import JobApplicationStatus
from app.models.sa.base import Base
from sqlalchemy import Column, DateTime, Integer, String, datetime


class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, nullable=False)
    applied_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    status = Column(String, nullable=False, default=JobApplicationStatus.APPLIED)
