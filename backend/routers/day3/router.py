from fastapi import APIRouter
from ...models import ChatRequest, ChatResponse

router = APIRouter(prefix="/api/day3", tags=["day3"])


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    return ChatResponse(reply=f"Chat (day 3): {request.message}")


@router.get("/health")
def health():
    return {"ok": True}
