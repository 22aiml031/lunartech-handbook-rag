import os
from openai import OpenAI
from dotenv import load_dotenv
from supabase_utils import similarity_search

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Set OpenRouter endpoint for OpenAI client
client.base_url = "https://openrouter.ai/api/v1"


def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding


def retrieve_context(query):
    query_embedding = get_embedding(query)
    results = similarity_search(query_embedding)
    return "\n\n".join(results)


def generate_answer(query, context):
    if not context:
        return "No relevant context found."

    prompt = f"""
You are an AI assistant.
Answer strictly using the provided context.

Context:
{context}

Question:
{query}

Answer:
"""

    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=1000
    )

    return response.choices[0].message.content
