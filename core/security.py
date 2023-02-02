"""
    Security module
"""
import bson
from uuid import UUID
from datetime import datetime, timedelta
from jose import JWTError, jwt
from pydantic import ValidationError
from fastapi import Depends, HTTPException, status, Security
from fastapi.security import OAuth2PasswordBearer
from config import settings
from core.database import users


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data: dict, token_type: str):
    """
    Create access token
    """
    to_encode = data.copy()
    if token_type == "access":
        expire = datetime.utcnow() + timedelta(hours=settings.ACCESS_TOKEN_EXPIRE_HOURS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        userid: str = payload.get("uuid")
        if email is None:
            raise credentials_exception
    except (JWTError, ValidationError):
        raise credentials_exception from None

    user = users.find_one(
        {"uuid": bson.Binary.from_uuid(UUID(hex=userid)), "email": email}, 
        {"_id": 0, "password": 0}
    )

    return {**user,  "disabled": False}


async def get_current_active_user(current_user = Security(get_current_user)):
    if current_user["disabled"]:
        raise HTTPException(status_code=400, detail="Inactive user")

    return current_user