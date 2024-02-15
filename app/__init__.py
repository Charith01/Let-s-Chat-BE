from fastapi import FastAPI, Request, status
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
app.include_router(controller.router,prefix=BASE_URL)

@app.exception_handler(Exception)
async def exception_handler(request: Request, error: Exception):
    """
    Handler method to override python exception
    :param request:
    :param error:
    :return:
    """
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        content=jsonable_encoder(
                            {"status": "Not Ok", "message": "Internal server error", "err_msg": str(error)}))