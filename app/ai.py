from ollama import chat

# This is AI model that explains HL7 v2 validation errors in simple English and provides suggested fixes.    
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

    response = chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]