import os
import requests

GROQ_API_KEY = os.getenv("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")  # Set this in your environment
MODEL = "llama3-8b-8192"

def generate_agenda_llm(title, topics, duration):
    prompt = f"""
Generate a professional meeting agenda for a meeting titled: '{title}'.
Topics to cover: {topics}.
Total duration: {duration}.
Structure the agenda into time blocks and include introductory and concluding remarks.
    """

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}]
        }
    )

    return response.json()["choices"][0]["message"]["content"]
