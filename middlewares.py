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
    except HTTPException as http_exception:
        return JSONResponse(
            status_code=http_exception.status_code,
            content={"message": http_exception.detail},
        )
    except Exception as exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": str(exception)},
        )
