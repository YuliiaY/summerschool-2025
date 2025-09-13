from typing import List, Literal
from pydantic import BaseModel, Field


class EchoRequest(BaseModel):
    message: str = Field(..., min_length=1, description="User input text")


class EchoResponse(BaseModel):
    reply: str


class ChatMessage(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str


class ChatRequest(BaseModel):
    messages: List[ChatMessage]


class ChatResponse(BaseModel):
    reply: str
