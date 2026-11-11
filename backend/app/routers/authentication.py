from fastapi import APIRouter

router = APIRouter(prefix="/authentication", tags=["Authentication"])


@router.post("/create")
def create_user():
    return {"message": "user created"}
