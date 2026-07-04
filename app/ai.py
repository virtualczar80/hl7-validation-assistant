import os
from ollama import Client

# Read Ollama host from environment variable
OLLAMA_HOST = os.getenv(
    "OLLAMA_HOST",
    "http://127.0.0.1:11434"
)

client = Client(host=OLLAMA_HOST)


def explain_error(error):

    prompt = f"""
You are an HL7 v2 healthcare integration expert.

Explain the following validation error in simple English.

Field: {error.field}
Field Name: {error.name}
Validation Error: {error.message}

Also provide a suggested fix.

Keep the response under 100 words.
"""

    response = client.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
