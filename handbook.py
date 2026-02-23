from rag import retrieve_context, generate_answer


def count_words(text):
    return len(text.split())


def generate_table_of_contents(topic):
    prompt = f"""
Generate a detailed table of contents for a 20,000-word handbook on {topic}.
Include 12-15 sections.
Return as numbered list.
"""
    return generate_answer(topic, prompt)


def generate_handbook(topic):
    full_text = ""
    
    toc_prompt = f"Generate a detailed table of contents for a 20,000-word handbook on {topic}."
    toc = generate_answer(topic, toc_prompt)
    full_text += toc + "\n\n"

    sections = [line for line in toc.split("\n") if line.strip()]

    for section in sections:
        context = retrieve_context(section)
        section_text = generate_answer(
            section,
            f"Write 1500-2000 words for section: {section}\nContext:\n{context}"
        )
        full_text += "\n\n" + section_text

    full_text += f"\n\nTotal Word Count: {count_words(full_text)}"
    return full_text
