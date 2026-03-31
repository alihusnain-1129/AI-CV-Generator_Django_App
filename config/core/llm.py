import requests
from django.conf import settings
import time

def call_llm(prompt: str) -> str:
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8000",
        "X-Title": "CV Generator"
    }

    payload = {
        "model": settings.OPENROUTER_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 500,
        "temperature": 0.5
    }

    # Retry logic in case of temporary provider errors
    for _ in range(3):
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()

        if "error" not in data:
            return data["choices"][0]["message"]["content"]

        time.sleep(1)

    return f"LLM Error: {data}"