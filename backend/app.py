from fastapi import FastAPI
from .routers import day1, day2, day3, day4, day5

app = FastAPI(title="summerschool-2025 API", version="0.1.0")

app.include_router(day1.router)
app.include_router(day2.router)
app.include_router(day3.router)
app.include_router(day4.router)
app.include_router(day5.router)


@app.get("/healthz")
def healthz():
    return {"status": "ok"}
