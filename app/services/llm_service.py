import httpx
from app.config import settings

async def get_bot_reply(user_message: str) -> str:
    headers = {
        "Authorization": f"Bearer {settings.API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "query": user_message,
        "context": "IT Helpdesk support assistant"
    }

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.post(
            "https://api.scaledown.ai/chat",
            headers=headers,
            json=payload
        )

    if response.status_code != 200:
        return "Sorry, service is temporarily unavailable."

    return response.json().get("response", "No response")
