__status__ = True
__version__ = "0.1.0"
__message__ = "Library Managment System API"

from typing_extensions import TypedDict


class Response(TypedDict):
    success: bool
    version: str
    message: str


response: Response = {
    "success": __status__,
    "version": __version__,
    "message": __message__,
}
