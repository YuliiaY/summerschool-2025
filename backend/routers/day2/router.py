from fastapi import APIRouter
from ...models import TaskRequest, TaskResponse

router = APIRouter(prefix="/api/day2", tags=["day2"])


@router.post("/echo", response_model=TaskResponse)
def echo(request: TaskRequest) -> TaskResponse:
    return TaskResponse(reply=f"Echo (day 2): {request.message}")


@router.get("/health")
def health():
    return {"ok": True}