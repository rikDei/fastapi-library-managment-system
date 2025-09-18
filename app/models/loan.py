from datetime import date

from sqlmodel import Field, SQLModel


class LoanBase(SQLModel):
    loan_date: date = Field(
        nullable=False,
        default=date.today(),
        description="The exact date when the book was checked out.",
    )
    due_date: date = Field(
        nullable=False, description="The date by which the book must be returned."
    )
    return_date: date | None = Field(
        nullable=True,
        default=None,
        description="The date when the book was actually returned. This field is NULL until the book is checked back in.",
    )


class Loan(LoanBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    book_id: int = Field(nullable=False, foreign_key="book.id")
    user_id: int = Field(nullable=False, foreign_key="user.id")


class LoanPublic(LoanBase):
    id: int
    title: str
    


class LoanCreate(LoanBase):
    pass
