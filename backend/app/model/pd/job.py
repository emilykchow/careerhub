from datetime import date

from app.schemas.base import CamelModel
from pydantic import BaseModel


class JobsRequest(BaseModel):
    job_titles: list[str] | None = None
    company_name: str | None = None
    salary_min: float | None = None
    location: str | None = None
    contract_time: str | None = None
    contract_type: str | None = None
    date_from: date | None = None
    date_to: date | None = None


class JobsResponse(CamelModel):
    id: int
    platform: str
    job_id: int
    job_title: str
    company_name: str
    salary: float | None = None
    location: str | None = None
    contract_time: str | None = None
    contract_type: str | None = None
    date_posted: date
