import streamlit as st
from app import dashboard, AI_Grading

st.set_page_config(page_title="AI Healthcare Simulation Dashboard", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Checklist Scoring", "AI Grading"])

# Route to selected page
if page == "Checklist Scoring":
    dashboard.run()
elif page == "AI Grading":
    AI_Grading.run()


