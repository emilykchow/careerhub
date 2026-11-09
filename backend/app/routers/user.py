from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/user")
def root():
    return {"message": "API is running"}
