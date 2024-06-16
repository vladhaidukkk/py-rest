from pydantic import BaseModel, SecretStr


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: SecretStr


class UserRead(UserBase):
    id: int
