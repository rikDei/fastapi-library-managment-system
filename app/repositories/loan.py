from datetime import date
from typing import Sequence

from sqlalchemy.engine.row import Row
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel.sql.expression import select

from app.models.book import Book
from app.models.loan import Loan


class LoanRepository:
    @staticmethod
    async def get_loan_by_id(session: AsyncSession, loan_id: int) -> Loan | None:
        stmt = select(Loan).where(Loan.id == loan_id)
        res = await session.scalar(stmt)
        return res

    @staticmethod
    async def get_loans_by_user_id(
        session: AsyncSession, user_id: int, offset: int, limit: int
    ):
        stmt = select(Loan, Book).join(Book).where(Loan.user_id == user_id).offset(offset).limit(limit)
        exec = await session.execute(stmt)
        res = exec.fetchall()
        return res

    @staticmethod
    async def get_loans_by_book_id(
        session: AsyncSession, book_id: int, offset: int, limit: int
    ) -> Sequence[Row[tuple[Loan]]]:
        stmt = select(Loan).where(Loan.book_id == book_id).offset(offset).limit(limit)
        exec = await session.execute(stmt)
        res = exec.fetchall()
        return res

    @staticmethod
    async def update_loan_return_date(
        session: AsyncSession, loan_id: int, return_date: date
    ) -> None:
        loan = await LoanRepository.get_loan_by_id(session=session, loan_id=loan_id)
        if not loan:
            raise
        loan.return_date = return_date
        session.add(loan)
        return None

    @staticmethod
    async def create_loan(session: AsyncSession, loan: Loan) -> None:
        session.add(loan)
        return None
