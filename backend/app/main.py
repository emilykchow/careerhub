from app.routers import users
from fastapi import FastAPI

app = FastAPI(title="My API", description="My FastAPI application", version="1.0.0")

app.include_router(users.router)
