import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    API_KEY = os.getenv("SCALE_DOWN_API_KEY")
    ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "").split(",")

settings = Settings()
