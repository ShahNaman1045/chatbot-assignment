from dotenv import load_dotenv
from openai import OpenAI

import os

load_dotenv()

client = OpenAI()

def generate_response(message):

    SYSTEM_PROMPT = f"""
        Respond as a political leader addressing a citizen.

        Your response must follow this structure exactly:

        Spanish:
        <response in Spanish>

        English:
        <translation in English>

        User message: {message}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
    )

    return response.choices[0].message.content
