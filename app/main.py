from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from app.config import settings
from app.routes.chat import router as chat_router

# 1️⃣ Create app FIRST
app = FastAPI(title="IT Helpdesk Chatbot")

# 2️⃣ CORS (safe for dev, AWS-ready)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],   # important
    allow_headers=["*"],
)

# 3️⃣ API routes
app.include_router(chat_router, prefix="/api")

# 4️⃣ Resolve frontend path safely
BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR.parent / "frontend"

# 5️⃣ Mount static frontend files
app.mount("/frontend", StaticFiles(directory=FRONTEND_DIR), name="frontend")

# 6️⃣ Serve frontend UI
@app.get("/", response_class=HTMLResponse)
def serve_frontend():
    index_file = FRONTEND_DIR / "index.html"
    return index_file.read_text(encoding="utf-8")

# 7️⃣ Health check
@app.get("/health")
def health_check():
    return {"status": "Backend running"}
