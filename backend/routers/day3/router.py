from fastapi import APIRouter
from ...models import TaskRequest, TaskResponse

router = APIRouter(prefix="/api/day3", tags=["day3"])


@router.post("/chat", response_model=TaskResponse)
def chat(request: TaskRequest) -> TaskResponse:
    return TaskResponse(reply=f"Chat (day 3): {request.message}")


@router.get("/health")
def health():
    return {"ok": True}
