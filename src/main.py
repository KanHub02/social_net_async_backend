import uvicorn

from decouple import config

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import origins

ALLOWED_HOSTS = config("ALLOWED_HOSTS")

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)


if __name__ == "__main__":
    uvicorn.run(app, host=ALLOWED_HOSTS, port=8088)