from app.constants import JobApplicationStatus
from app.models.sa.base import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float, datetime,


class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    job_id = Column(Integer, nullable=False)
    platform = Column(String, nullable=False)
    job_title = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
    salary = Column(Float, nullable=True)
    location = Column(String, nullable=True)
    application_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    status = Column(String, nullable=False, default=JobApplicationStatus.APPLIED)
