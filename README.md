# LunarTech Handbook RAG Chat App

This project implements a Retrieval-Augmented Generation (RAG) system using:

- Streamlit
- Supabase (pgvector)
- OpenRouter / LLM
- PDF ingestion and chunking
- Semantic search

## Setup Instructions

1. Clone the repository
2. Create virtual environment
3. Install dependencies:
   pip install -r requirements.txt
4. Add your .env file with API keys
5. Run:
   streamlit run app.py

## Features

- Upload PDFs
- Vector embeddings
- Semantic similarity search
- Context-grounded answers
- Handbook generation
