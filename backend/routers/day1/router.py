import os

from dotenv import load_dotenv
from fastapi import APIRouter
from openai import OpenAI

from ...models import ChatRequest, ChatResponse

load_dotenv()
client = OpenAI(

  base_url="https://openrouter.ai/api/v1",

  api_key=os.getenv("OPENROUTER_API_KEY"),

)

router = APIRouter(prefix="/api/day1", tags=["day1"])


@router.post("/echo", response_model=ChatResponse)
def echo(request: ChatRequest) -> ChatResponse:
    return ChatResponse(reply=f"Echo (day 1): {request.message}")


@router.post("/film_reviewer", response_model=ChatResponse)
def film_reviewer(request: ChatRequest) -> ChatResponse:
    print(request.message)
    promt = f"""You are a popular film citic. Be literal and consistent.
        Write a review for a film in the given language. 
        Here is the film and the language: {request.message}"""
    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[
            {
                "role": "user",
                "content": promt
            }
        ]
    )

    return ChatResponse(reply=f"Review: {completion}")


@router.get("/health")
def health():
    return {"ok": True}
