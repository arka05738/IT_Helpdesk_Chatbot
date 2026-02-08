from fastapi import APIRouter, HTTPException
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.llm_service import get_bot_reply

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        reply = await get_bot_reply(request.message)
        return ChatResponse(reply=reply)
    except Exception as e:
        print("ERROR:", e)   # 👈 important
        raise HTTPException(status_code=500, detail=str(e))
