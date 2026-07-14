from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.memory import router as memory_router

app = FastAPI(title="AI Memory Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # We'll tighten this later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(memory_router)


@app.get("/")
def root():
    return {"status": "running"}