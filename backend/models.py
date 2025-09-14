from pydantic import BaseModel, Field


class TaskRequest(BaseModel):
    message: str = Field(..., min_length=1, description="User input text")


class TaskResponse(BaseModel):
    reply: str