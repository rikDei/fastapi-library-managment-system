from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.settings.app import AppSettings
from app.routers import book, loan, user

app_settings = AppSettings()
app = FastAPI(
    debug=app_settings.debug,
    title=app_settings.title,
    version=app_settings.version,
    openapi_url=app_settings.openapi_url,
    docs_url=app_settings.docs_url,
    redoc_url=app_settings.redoc_url,
    openapi_prefix=app_settings.openapi_prefix,
    root_path=app_settings.api_prefix,
)

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
app.include_router(user.router)
app.include_router(loan.router)
