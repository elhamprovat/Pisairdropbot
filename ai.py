import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def create_post(link: str):
    prompt = f"""
You are a crypto content writer.

Create a professional Telegram post for this airdrop.

Rules:
- Attractive title
- Use emojis
- Maximum 120 words
- End with these hashtags:
#Airdrop #Crypto #Free
- Put this link at the end:

{link}
"""

    response = model.generate_content(prompt)
    return response.text
