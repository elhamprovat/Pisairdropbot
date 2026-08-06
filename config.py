import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing!")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing!")

if not CHANNEL_USERNAME:
    raise ValueError("CHANNEL_USERNAME is missing!")
