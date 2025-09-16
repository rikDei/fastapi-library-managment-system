from collections.abc import Sequence

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel.sql.expression import select

from app.models.book import Book


class BookRepository:
    @staticmethod
    async def get_books(session: AsyncSession, limit: int = 100) -> Sequence[Book]:
        stmt = select(Book).limit(limit)
        exec = await session.scalars(stmt)
        results = exec.fetchall()
        return results

    @staticmethod
    async def get_book_by_id(session: AsyncSession, book_id: int) -> Book | None:
        stmt = select(Book).where(Book.id == book_id)
        result = await session.scalar(stmt)
        return result

    @staticmethod
    async def get_book_by_isbn(session: AsyncSession, isbn_code: str) -> Book | None:
        stmt = select(Book).where(Book.isbn_code == isbn_code)
        result = await session.scalar(stmt)
        return result

    @staticmethod
    async def create_book(session: AsyncSession, book: Book):
        session.add(book)
        return None

    @staticmethod
    async def delete_book_by_id(session: AsyncSession, book_id: int):
        book = await session.get(Book, book_id)
        if book:
            await session.delete(book)
        return None

    @staticmethod
    async def lend_book(session: AsyncSession, book_id: int, num_copies_lent: int):
        book = await session.get(Book, book_id)
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="No book found"
            )
        available_copies = int(book.available_copies)
        if not available_copies:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="No available copies"
            )
        else:
            new_copies = available_copies - num_copies_lent
            if new_copies < 0:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Can't lend more copies than available.",
                )
            book.available_copies = new_copies

        return None

    @staticmethod
    async def return_book(session: AsyncSession, book_id: int, num_copies_returned: int):
        book = await session.get(Book, book_id)
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="No book found"
            )
        available_copies = int(book.available_copies)
        total_copies = int(book.total_copies)
        new_copies = available_copies + num_copies_returned
        if new_copies > total_copies:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Can't add more copies than total.",
            )
        book.available_copies = new_copies
        return None
