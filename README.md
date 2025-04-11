# 🩺 AI Healthcare Simulation Dashboard

AI-powered Streamlit dashboard that analyzes healthcare simulation survey results, performance checklist data, and generates automated reports for instructors and simulation center teams.

---

## 🚀 Features

- Upload simulation survey CSV data
- Analyze Likert scale & performance metrics
- Run sentiment analysis on open-ended comments
- Generate word clouds for feedback trends
- Auto-generate summary insights
- Export PDF-ready report for debriefing

---

## 🧰 Technologies Used

- Python
- Streamlit
- Pandas
- Matplotlib
- TextBlob (Sentiment Analysis)
- WordCloud
- FPDF (PDF Report Generation)

---

## 🗂 Folder Structure

```
ai-healthcare-sim-dashboard/
│
├── app.py                 # Main Streamlit App
├── requirements.txt      # Python dependencies
├── checklist.csv         # Example expected checklist
├── sample_survey.csv     # Example user survey data
├── score.py              # Performance scoring logic
├── utils.py              # Helper functions
├── report_template.pdf   # Optional PDF template
└── README.md             # This file
```

---

## ⚙️ Getting Started

1. Clone the repository:
```bash
git clone https://github.com/qsmith87/ai-healthcare-sim-dashboard.git
cd ai-healthcare-sim-dashboard
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

4. Upload your CSV files and explore the dashboard.

---

## 📊 Example Dashboard Screenshot

*Add your Streamlit dashboard screenshot here.*

---

## 🛠 Future Improvements

- Add real-time LLEAP / SimCapture API integration
- Role-based dashboard filters (nurses, med students, residents)
- Customizable PDF branding
- Performance scoring AI model
- Cloud-hosted version

---

## 📬 Contact

Quentin Smith  
Simulation Technologist | AI in Healthcare & Aerospace  
[LinkedIn](https://www.linkedin.com/in/quentin-smith-b23b5847/)  
GitHub: [@qsmith87](https://github.com/qsmith87)

---
