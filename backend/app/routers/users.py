from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/create")
def create_user():
    return {"message": "user created"}
