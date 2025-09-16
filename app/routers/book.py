from collections.abc import Sequence

from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from app.core.dependencies import DBSession
from app.models.book import Book, BookCreate, BookPublic
from app.repositories.book import BookRepository

router = APIRouter(tags=["Book"], prefix="/book")


@router.get("", status_code=status.HTTP_200_OK, response_model=list[BookPublic])
async def get_books(session: DBSession) -> Sequence[Book]:
    try:
        books = await BookRepository.get_books(session=session)
        if not books:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="No book found"
            )
        return books
    except Exception as e:
        raise e


@router.get("/id/{book_id}", status_code=status.HTTP_200_OK)
async def get_book_by_id(session: DBSession, book_id: int):
    try:
        book = await BookRepository.get_book_by_id(session=session, book_id=book_id)
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="No book found"
            )
        return JSONResponse(content=dict(book))
    except Exception as e:
        raise e


@router.get("/isbn/{isbn_code}")
async def get_book_by_isbn_code(session: DBSession, isbn_code: str):
    try:
        book = await BookRepository.get_book_by_isbn(
            session=session, isbn_code=isbn_code
        )
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="No book found"
            )
        return JSONResponse(content=dict(book))
    except Exception as e:
        raise e


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_book(session: DBSession, book: BookCreate):
    try:
        db_book = Book.model_validate(book)
        await BookRepository.create_book(session=session, book=db_book)
    except Exception as e:
        raise e


@router.delete("/id/{}")
async def delete_book(session: DBSession, book_id: int):
    try:
        await BookRepository.delete_book_by_id(session=session, book_id=book_id)
    except Exception as e:
        raise e


@router.patch("/lend/{book_id}/num-copies-lent/{num_copies_lent}")
async def lend_book(session: DBSession, book_id: int, num_copies_lent: int = 1):
    # Check available copies
    try:
        await BookRepository.lend_book(
            session=session, book_id=book_id, num_copies_lent=num_copies_lent
        )
    except Exception as e:
        raise e


@router.patch("/return/{book_id}/num-copies-returned/{num_copies_returned}")
async def return_book(session: DBSession, book_id: int, num_copies_returned: int = 1):
    try:
        await BookRepository.return_book(
            session=session, book_id=book_id, num_copies_returned=num_copies_returned
        )
    except Exception as e:
        raise e
