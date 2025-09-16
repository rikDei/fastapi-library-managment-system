from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.container import container
# from app.core.security import HTTPTokenHeader

# token_security = HTTPTokenHeader(
#     name="Authorization",
#     scheme_name="JWT Token",
#     description="Token Format: `Token xxxxxx.yyyyyyy.zzzzzz`",
#     raise_error=True,
# )
# token_security_optional = HTTPTokenHeader(
#     name="Authorization",
#     scheme_name="JWT Token",
#     description="Token Format: `Token xxxxxx.yyyyyyy.zzzzzz`",
#     raise_error=False,
# )

# JWTToken = Annotated[str, Depends(token_security)]
# JWTTokenOptional = Annotated[str, Depends(token_security_optional)]

DBSession = Annotated[AsyncSession, Depends(container.session)]
