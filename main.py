from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apis.api_base import api_router

def include_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

def include_router(app: FastAPI):
    app.include_router(api_router)

def start_application():
    app = FastAPI("MJ_app", version="1.0")
    include_cors(app)
    include_router(app)
    return app

app = start_application()