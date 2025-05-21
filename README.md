# AI Healthcare Simulation Dashboard

This is a Streamlit-based AI-powered grading tool for clinical simulation post-encounter notes. It uses an LLM via OpenRouter to evaluate learner notes based on a customizable rubric.

## Features

- 📄 Upload learner post-encounter notes
- 🤖 AI-driven scoring on 7 key clinical dimensions
- 💡 Real-time feedback with rubric-based evaluation
- 🔐 Secure API key management via `.env`

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Healthcare-Sim-Dashboard.git
cd AI-Healthcare-Sim-Dashboard
```

### 2. Set up your environment

Install required Python packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file with your OpenRouter API key:

```bash
echo "OPENROUTER_API_KEY=your-api-key-here" > .env
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## File Structure

```
app.py                    # Main launcher for Streamlit app
app/
  ├── ai_grading.py       # AI grading logic via OpenRouter
  ├── dashboard.py        # Checklist scoring module (if used)
  ├── score.py            # Supporting scoring engine
  └── __init__.py
data/
  ├── checklist.csv        # Example rubric checklist
  └── sample_simulation_data.csv  # Sample student note
.env                      # API key (excluded from GitHub)
```

## 📬 Contact

Quentin Smith  
Simulation Technologist | AI in Healthcare & Aerospace  
[LinkedIn](https://www.linkedin.com/in/quentin-smith-b23b5847/)  
GitHub: [@qsmith87](https://github.com/qsmith87)

---
