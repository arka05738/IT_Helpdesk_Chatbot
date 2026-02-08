import os
from openai import OpenAI, RateLimitError

DEMO_MODE = os.getenv("DEMO_MODE", "false").lower() == "true"

client = OpenAI()

def generate_answer(query: str) -> str:
    if DEMO_MODE:
        return (
            "This is a demo response.\n\n"
            "In production, the system uses a cloud-based "
            "Large Language Model to answer IT helpdesk queries."
        )

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=query
        )
        return response.output[0].content[0].text

    except RateLimitError:
        return "Service temporarily unavailable. Please try again later."
