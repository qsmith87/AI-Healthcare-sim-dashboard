import streamlit as st
import pandas as pd
import os
from .score import evaluation_engine

# Define the path to the checklist
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
checklist_path = os.path.join(BASE_DIR, "..", "data", "checklist.csv")

# Streamlit view function
def run():
    st.title("🩺 AI-Enhanced Clinical Simulation Scoring Tool")

    try:
        expected = pd.read_csv(checklist_path)
    except FileNotFoundError:
        st.error("❌ Could not load the checklist. Please make sure 'checklist.csv' is located in the 'data/' folder.")
        return

    uploaded_file = st.file_uploader("📤 Upload your simulation steps CSV", type="csv")

    if uploaded_file:
        try:
            actual = pd.read_csv(uploaded_file)
            score, total, feedback = evaluation_engine(expected, actual)

            st.subheader(f"🧾 Score: {score} / {total}")
            st.write("### 🧠 Feedback")
            for f in feedback:
                st.write(f)
        except Exception as e:
            st.error(f"An error occurred while processing your file: {e}")
