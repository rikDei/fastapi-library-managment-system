from pydantic.networks import EmailStr
from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    username: str = Field(nullable=False, unique=True)
    email: EmailStr = Field(nullable=False, unique=True)


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str = Field(nullable=False)

class UserPublic(UserBase):
    pass


class UserCreate(UserBase):
    password: str = Field(nullable=False)


class UserUpdate(UserBase):
    password: str = Field(nullable=False)
