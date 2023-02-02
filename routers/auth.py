"""
    Authentication Router

"""
from passlib.hash import pbkdf2_sha256
from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from core.database import users
from core.security import create_access_token


router = APIRouter()

@router.post('/login', summary="Performs authentication")
async def log_in(request: OAuth2PasswordRequestForm = Depends()):
    """
        Performs authentication and returns the authentication token to keep the user
        logged in for longer time.

        Provide **Username** and **Password** to log in.

    """
    user = users.find_one({"email": request.username.lower()})

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid credentials"
        )
    if not pbkdf2_sha256.verify(request.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect password"
        )

    access_token = create_access_token(
        data={
            "sub": user["email"],
            "uuid": user["uuid"].hex(),
        },
        token_type="access")

    return {"access_token": access_token, "token_type": "bearer"}
