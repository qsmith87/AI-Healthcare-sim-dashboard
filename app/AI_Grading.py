import streamlit as st
import os
import requests
from dotenv import load_dotenv

# Load environment variables (for OpenRouter API key)
load_dotenv()
OR_API_KEY = os.getenv("OPENROUTER_API_KEY")

# OpenRouter endpoint (uses OpenAI-compatible format)
OR_API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {OR_API_KEY}",
    "Content-Type": "application/json"
}

# OpenRouter chat-based LLM query function
def query_openrouter(prompt, model="mistralai/mistral-7b-instruct:free"):
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are an expert OSCE grader evaluating student clinical notes."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 150
    }
    try:
        response = requests.post(OR_API_URL, headers=HEADERS, json=payload)
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"⚠️ Error: {e}"

# AI grading logic using OpenRouter
def evaluate_note_with_ai(note_text, rubric_items):
    feedback = []
    score = 0
    total = len(rubric_items)

    for item in rubric_items:
        prompt = (
            f"Does this clinical note show evidence of: {item}?\n"
            f"Answer Yes or No with a short reason.\n\n"
            f"Note: {note_text}"
        )

        reply = query_openrouter(prompt)

        if reply.lower().startswith("yes"):
            feedback.append(f"✅ {item} — {reply}")
            score += 1
        elif reply.lower().startswith("no"):
            feedback.append(f"❌ {item} — {reply}")
        else:
            feedback.append(f"⚠️ No response for '{item}'. Got: '{reply}'")

    return score, total, feedback

# Streamlit interface
def run():
    st.title("🧠 AI Grading - Post-Encounter Note Evaluation (OpenRouter Edition)")
    st.write("Upload a learner's clinical note and let an OpenRouter-hosted LLM evaluate it using rubric-based logic.")

    rubric_items = [
        "Accurate primary diagnosis",
        "Complete patient history",
        "Clear differential diagnosis",
        "Detailed physical exam findings",
        "Appropriate diagnostic plan",
        "Well-structured treatment plan",
        "Logical clinical reasoning"
    ]

    note_text = st.text_area("Paste the post-encounter note here:", height=300)

    if st.button("Evaluate Note") and note_text:
        with st.spinner("Evaluating using OpenRouter LLM..."):
            score, total, feedback = evaluate_note_with_ai(note_text, rubric_items)

        st.subheader(f"🧾 Score: {score} / {total}")
        st.write("### 🧠 Feedback")
        for f in feedback:
            st.write(f)

    st.write("---")
    st.caption("Note: This version uses OpenRouter.ai with mistralai/mistral-7b-instruct:free. Set your OPENROUTER_API_KEY in your .env file.")

