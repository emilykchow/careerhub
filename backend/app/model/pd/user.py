from pydantic import BaseModel, ConfigDict


class UserBaseSchema(BaseModel):
    email: str
    full_name: str | None = None


class UserResponseSchema(UserBaseSchema):
    id: int

    model_config = ConfigDict(from_attributes=True)
