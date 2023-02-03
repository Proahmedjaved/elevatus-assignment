"""
    This file contains the fastapi middlewares for the project.
"""

from fastapi import Request, status
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

def exception_handling_middleware(request: Request, call_next):
    """
        This middleware handles the exceptions raised by the application.
    """
    try:
        response = call_next(request)
        return response
    except Exception as exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": str(exception)},
        )
