import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_answer(question, context):

    prompt = f"""
You are the DevDesk AI Support Engineer.

Answer the customer's question using only the
provided knowledge base context.

Rules:
- Do not invent information.
- Do not invent API endpoints or product features.
- If the context does not contain enough information,
  clearly say that the available documentation is
  insufficient and recommend escalation.
- Never ask for passwords, API keys, access tokens,
  or other authentication secrets.
- Give clear and practical troubleshooting steps
  when supported by the documentation.

CUSTOMER QUESTION:

{question}

KNOWLEDGE BASE CONTEXT:

{context}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text