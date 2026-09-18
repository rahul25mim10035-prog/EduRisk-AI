from src.predictor import load_model,predict_student

def test_prediction():
    model=load_model()
    values={
        "attendance_pct":80,"study_hours_per_day":3,
        "assignment_score_pct":75,"internal_marks_pct":70,
        "previous_gpa":7.5,"previous_backlogs":0,
        "sleep_hours":7,"class_participation_pct":70
    }
    risk,prob=predict_student(model,values)
    assert risk in {"Low","Medium","High"}
    assert isinstance(prob,dict)
