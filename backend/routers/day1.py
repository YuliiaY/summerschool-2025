from fastapi import APIRouter
from ..models import EchoRequest, EchoResponse

router = APIRouter(prefix="/api/day1", tags=["day1"]) 


@router.post("/echo", response_model=EchoResponse)
def echo(request: EchoRequest) -> EchoResponse:
    return EchoResponse(reply=f"Echo (day 1): {request.message}")


@router.get("/health")
def health():
    return {"ok": True}
