from fastapi import APIRouter
from ..models import ChatRequest, ChatResponse

router = APIRouter(prefix="/api/day5", tags=["day5"]) 


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    last_user = next((m.content for m in reversed(request.messages) if m.role == "user"), "" )
    return ChatResponse(reply=f"Stub (day 5): received '{last_user}'.")


@router.get("/health")
def health():
    return {"ok": True}
