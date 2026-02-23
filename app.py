import streamlit as st
from dotenv import load_dotenv
from pdf_utils import extract_text_from_pdf, chunk_text
from rag import get_embedding, generate_answer, retrieve_context
from supabase_utils import store_embedding
from handbook import generate_handbook

load_dotenv()

st.title("LunarTech Handbook RAG Chat App")

uploaded_files = st.file_uploader("Upload PDF documents", type="pdf", accept_multiple_files=True)

if uploaded_files:
    if st.button("Process PDFs"):
        for file in uploaded_files:
            text = extract_text_from_pdf(file)
            chunks = chunk_text(text)

            for chunk in chunks:
                embedding = get_embedding(chunk)
                store_embedding(chunk, embedding)

        st.success("PDFs processed and embeddings stored.")

st.subheader("Ask questions about your documents:")
user_input = st.text_input("Your question or command:")

if user_input:
    if "create a handbook" in user_input.lower():
        topic = user_input.replace("create a handbook", "").strip()
        handbook = generate_handbook(topic)
        st.write(handbook)
    else:
        context = retrieve_context(user_input)
        answer = generate_answer(user_input, context)
        st.write(answer)
