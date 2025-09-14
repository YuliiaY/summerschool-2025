from fastapi import APIRouter
from ...models import TaskRequest, TaskResponse

router = APIRouter(prefix="/api/day4", tags=["day4"])


@router.post("/chat", response_model=TaskResponse)
def chat(request: TaskRequest) -> TaskResponse:
    return TaskResponse(reply=f"Chat (day 4): {request.message}")


@router.get("/health")
def health():
    return {"ok": True}
