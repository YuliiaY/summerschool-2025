from fastapi import APIRouter
from ..models import ChatRequest, ChatResponse

router = APIRouter(prefix="/api/day3", tags=["day3"]) 


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    last_user = next((m.content for m in reversed(request.messages) if m.role == "user"), "" )
    return ChatResponse(reply=f"Stub (day 3): received '{last_user}'.")


@router.get("/health")
def health():
    return {"ok": True}
