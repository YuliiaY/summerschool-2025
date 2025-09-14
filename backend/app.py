from fastapi import FastAPI
from .routers import day1

app = FastAPI(title="summerschool-2025 API", version="0.1.0")

app.include_router(day1.router)


@app.get("/healthz")
def healthz():
    return {"status": "ok"}
