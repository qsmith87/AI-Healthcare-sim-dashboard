import os
import pandas as pd

# Define base directory for consistent path resolution
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load expected checklist from the 'data' directory
expected_path = os.path.join(BASE_DIR, "..", "data", "checklist.csv")
expected = pd.read_csv(expected_path)

# Score each step
def evaluation_engine(expected_df, actual_df):
    score = 0
    feedback = []

    for i in range(len(expected_df)):
        if i < len(actual_df) and expected_df.iloc[i]["Action"] == actual_df.iloc[i]["Action"]:
            score += 1
            feedback.append(f"✅ Step {i+1} correct: {expected_df.iloc[i]['Action']}")
        else:
            actual_action = actual_df.iloc[i]["Action"] if i < len(actual_df) else "N/A"
            feedback.append(f"❌ Step {i+1} incorrect. Expected: {expected_df.iloc[i]['Action']}, Got: {actual_action}")

    total = len(expected_df)
    return score, total, feedback
