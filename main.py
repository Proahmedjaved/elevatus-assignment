"""
    main.py
    ~~~~~~~
    This file is used to store the configuration of the application.

"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from routers.routers import api_router

from middlewares import exception_handling_middleware


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="This is elevatus assignment",
)

app.middleware(middleware_type="http")(exception_handling_middleware)

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", include_in_schema=False)
async def root():
    return {"message": "Hello World"}

app.include_router(api_router)