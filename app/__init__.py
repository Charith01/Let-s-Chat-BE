from fastapi import FastAPI, Request, status
from starlette.middleware.cors import CORSMiddleware

from app import controller
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

VERSION = "v1"
BASE_URL = f"/api/chat-be/{VERSION}"
app = FastAPI(
    title="Chat BE",
    version="1.0",
    description="Chat BE APIs",
    docs_url=f"{BASE_URL}/public/doc",
    redoc_url=f"{BASE_URL}/public/redoc",
)
origins = [
    "http://localhost:3000",  # Add your React app's origin here
    # Add more origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(controller.router,prefix=BASE_URL)

@app.exception_handler(Exception)
async def exception_handler(error: Exception):
    """
    Handler method to override python exception
    :param request:
    :param error:
    :return:
    """
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        content=jsonable_encoder(
                            {"status": "Not Ok", "message": "Internal server error", "err_msg": str(error)}))