from src.predictor import load_model, predict_student
from src.explainability import explain
from src.intervention import recommendations


def read_float(prompt, minimum, maximum):
    while True:
        try:
            value = float(input(prompt))
            if minimum <= value <= maximum:
                return value
            print(f"Please enter a value between {minimum} and {maximum}.")
        except ValueError:
            print("Please enter a valid number.")


def read_int(prompt, minimum, maximum):
    while True:
        try:
            value = int(input(prompt))
            if minimum <= value <= maximum:
                return value
            print(f"Please enter an integer between {minimum} and {maximum}.")
        except ValueError:
            print("Please enter a valid integer.")


def main():
    print("\n" + "=" * 42)
    print("              EduRisk AI")
    print(" Student Academic Risk Prediction System")
    print("=" * 42)
    print("Enter the student's academic and learning indicators.\n")

    values = {
        "attendance_pct": read_float("Attendance (%) [0-100]: ", 0, 100),
        "study_hours_per_day": read_float("Study hours/day [0-12]: ", 0, 12),
        "assignment_score_pct": read_float("Assignment score (%) [0-100]: ", 0, 100),
        "internal_marks_pct": read_float("Internal marks (%) [0-100]: ", 0, 100),
        "previous_gpa": read_float("Previous GPA [0-10]: ", 0, 10),
        "previous_backlogs": read_int("Previous backlogs [0-10]: ", 0, 10),
        "sleep_hours": read_float("Sleep hours/day [0-12]: ", 0, 12),
        "class_participation_pct": read_float("Class participation (%) [0-100]: ", 0, 100),
    }

    try:
        model = load_model()
        risk, probabilities = predict_student(model, values)
    except FileNotFoundError:
        print("\nModel not found. Run `python3 train.py` first.")
        return

    print("\n" + "-" * 42)
    print(f"Predicted Academic Risk: {risk.upper()}")
    print("-" * 42)

    if probabilities:
        print("Prediction Probabilities:")
        for label, probability in probabilities.items():
            print(f"  {label:<7}: {probability * 100:6.2f}%")

    print("\nKey Indicators:")
    for item in explain(values):
        print(f"  - {item}")

    print("\nSuggested Intervention:")
    for item in recommendations(values, risk):
        print(f"  - {item}")

    print("\nNote: This prototype uses a synthetic demonstration dataset.")
    print("Its prediction should not be used as the sole basis for real academic decisions.")


if __name__ == "__main__":
    main()
