import os

from openai import OpenAI


SYSTEM_PROMPT = (
    "You are a helpful Indian public welfare assistant. "
    "You explain PM-KISAN, scholarships, health schemes, and complaint filing clearly. "
    "If you are unsure, say so and recommend checking official portals."
)


def generate_with_groq(user_query: str) -> str:
    api_key = os.getenv("GROQ_API_KEY")
    model = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
    if not api_key:
        return (
            "GROQ_API_KEY is not configured. "
            "Please set it to enable AI answers. For now, use menu options for guided support."
        )

    client = OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")
    completion = client.chat.completions.create(
        model=model,
        temperature=0.2,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query},
        ],
    )
    return completion.choices[0].message.content or "Sorry, I could not generate a response."
