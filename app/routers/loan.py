from typing import Sequence


from sqlalchemy.engine.row import Row


from app.models.book import Book


from datetime import date

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from app.core.dependencies import DBSession, UserPubDep
from app.models.loan import Loan, LoanCreate, LoanPublic
from app.repositories.book import BookRepository
from app.repositories.loan import LoanRepository

router = APIRouter(tags=["Loan"], prefix="/loan")


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_loan(
    session: DBSession, loan_create: LoanCreate, current_user: UserPubDep, book_id: int
):
    loan = Loan(
        book_id=book_id,
        user_id=current_user.id,
        loan_date=loan_create.loan_date,
        due_date=loan_create.due_date,
    )
    try:
        await BookRepository.lend_book(session=session, book_id=book_id)
        await LoanRepository.create_loan(session=session, loan=loan)
        return JSONResponse(content={"message": "Loan created."})
    except Exception as e:
        raise e


@router.patch("/return", status_code=status.HTTP_204_NO_CONTENT)
async def return_loan(session: DBSession, loan_id: int):
    today = date.today()
    try:
        loan = await LoanRepository.get_loan_by_id(session=session, loan_id=loan_id)
        if loan:
            await LoanRepository.update_loan_return_date(
                session=session, loan_id=loan_id, return_date=today
            )
            await BookRepository.return_book(session=session, book_id=loan.book_id)
        else:
            raise HTTPException(status_code=404, detail="Loan not found")
    except Exception as e:
        raise e


@router.get("/my-loans")
async def get_loans_by_user_id(
    session: DBSession, current_user: UserPubDep, offset: int = 0, limit: int = 20
):
    try:
        loans = await LoanRepository.get_loans_by_user_id(
            session=session, user_id=current_user.id, offset=offset, limit=limit
        )
        return [LoanPublic(**loan[0].model_dump(), title=loan[1].title) for loan in loans]
    except Exception as e:
        raise e
