import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Supabase URL or Key not found in environment variables.")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def store_embedding(content: str, embedding: list):
    """
    Store content and its embedding into Supabase.
    """
    try:
        response = supabase.table("handbook_chunks").insert({
            "content": content,
            "embedding": embedding
        }).execute()

        if response.data:
            return True
        else:
            print("Insert failed:", response)
            return False

    except Exception as e:
        print("SUPABASE INSERT ERROR:", e)
        return False


def similarity_search(query_embedding: list, top_k: int = 5):
    """
    Perform vector similarity search using RPC function.
    """
    try:
        response = supabase.rpc(
            "match_handbook_chunks",
            {
                "query_embedding": query_embedding,
                "match_count": top_k
            }
        ).execute()

        if response.data:
            return [item["content"] for item in response.data]
        else:
            print("No matching results found.")
            return []

    except Exception as e:
        print("SUPABASE SEARCH ERROR:", e)
        return []
