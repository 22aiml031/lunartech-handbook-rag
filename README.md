# 🚀 LunarTech Handbook RAG Chat App

An end-to-end **Retrieval-Augmented Generation (RAG)** system that enables intelligent question answering and handbook generation from uploaded PDF documents.

Built as part of the **AI Engineering Apprenticeship Assignment**.

---

## 📌 Project Overview

This project implements a complete RAG pipeline that:

- 📄 Ingests PDF documents
- ✂️ Splits them into semantic chunks
- 🔢 Generates vector embeddings
- 🗄 Stores embeddings in Supabase (pgvector)
- 🔍 Performs semantic similarity search
- 🤖 Uses an LLM to generate grounded responses
- 📘 Generates structured handbook content

The system ensures responses are grounded in uploaded documents rather than relying solely on model memory.

---

## 🧠 Architecture

User Query  
⬇  
Generate Query Embedding  
⬇  
Retrieve Similar Chunks from Supabase  
⬇  
Inject Context into Prompt  
⬇  
LLM Generates Grounded Answer  

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Streamlit |
| Backend | Python |
| Vector Database | Supabase (Postgres + pgvector) |
| Embeddings | LLM Embedding API |
| LLM | GPT / OpenRouter compatible models |
| PDF Processing | pdfplumber |
| Token Handling | tiktoken |

---

## 📂 Project Structure
lunartech-handbook-rag/
│
├── app.py # Streamlit UI
├── rag.py # Embedding + LLM logic
├── handbook.py # Handbook generation logic
├── pdf_utils.py # PDF loading & chunking
├── supabase_utils.py # Supabase DB operations
├── requirements.txt
└── README.md

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt

OPENAI_API_KEY/openrouter_api_key=your_api_key
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key

streamlit run app.py

📄 Features
✅ PDF Upload & Processing
Supports large PDF documents
Automatic chunking
Token-aware splitting
✅ Vector Storage
Uses pgvector extension in Supabase
Efficient cosine similarity search
✅ Semantic Retrieval
Finds most relevant chunks
Reduces hallucination
Improves factual grounding
✅ Context-Aware Answer Generation
Injects retrieved content into prompt
Produces document-grounded answers
✅ Handbook Generation
Generates structured content
Can create topic summaries
Supports short and long formats


Supabase Schema
create extension if not exists vector;

create table handbook_chunks (
  id bigserial primary key,
  content text,
  embedding vector(1536)
);
