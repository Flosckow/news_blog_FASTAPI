from fastapi_users import FastAPIUsers
from fastapi import FastAPI, Response, Request

from api import routers
from core.config import BACKEND_CORS_ORIGINS
from fastapi.middleware.cors import CORSMiddleware

from db.session import database


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     response = Response("Internal server error", status_code=500)
#     try:
#         request.state.db = SessionLocal()
#         response = await call_next(request)
#     finally:
#         request.state.db.close()
#     return response
#

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(routers.api_router)

