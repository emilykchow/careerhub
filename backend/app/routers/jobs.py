from app.model.pd.job import JobsRequest, JobsResponse
from app.services.jobs import get_jobs
from fastapi import APIRouter

router = APIRouter(prefix="/jobs", tags=["Jobs"])


@router.post("/", response_model=JobsResponse)
def fetch_jobs(jobs_request: JobsRequest):
    return get_jobs(jobs_request)
