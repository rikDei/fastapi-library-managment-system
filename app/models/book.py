from datetime import date

from sqlmodel import Field, SQLModel


class BookBase(SQLModel):
    isbn_code: str = Field(nullable=False)
    title: str = Field(index=True)
    author: str = Field(index=True)
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
