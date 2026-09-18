from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT_DIR / "data" / "student_performance.csv"
MODEL_PATH = ROOT_DIR / "models" / "trained_model.pkl"
RESULTS_PATH = ROOT_DIR / "models" / "model_results.csv"

TARGET = "risk_level"
FEATURES = [
    "attendance_pct",
    "study_hours_per_day",
    "assignment_score_pct",
    "internal_marks_pct",
    "previous_gpa",
    "previous_backlogs",
    "sleep_hours",
    "class_participation_pct",
]
