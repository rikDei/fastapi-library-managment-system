from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import book

app = FastAPI()

origins = [
    "https://localhost",
    "https://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(book.router)
