from datetime import date

from sqlmodel import Field, SQLModel


class BookBase(SQLModel):
    isbn_code: str = Field(index=True, nullable=False)
    title: str = Field(index=True, nullable=False)
    author: str = Field(nullable=False)
    publication_year: date = Field(nullable=False)
    genre: str = Field(nullable=True)


class Book(BookBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    total_copies: int = Field(nullable=False)
    available_copies: int = Field(nullable=True)


class BookPublic(BookBase):
    total_copies: int = Field(nullable=False)
    available_copies: int = Field(nullable=True)


class BookCreate(BookBase):
    total_copies: int = Field(nullable=False)
    available_copies: int = Field(nullable=False)


class BookUpdate(BookBase):
    total_copies: int = Field(nullable=True)
    available_copies: int = Field(nullable=True)
