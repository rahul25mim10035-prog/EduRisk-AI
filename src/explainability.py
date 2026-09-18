def explain(values):
    reasons=[]
    if values["attendance_pct"]<75: reasons.append("Attendance is below 75%.")
    if values["study_hours_per_day"]<2: reasons.append("Daily study time is relatively low.")
    if values["assignment_score_pct"]<60: reasons.append("Assignment performance needs improvement.")
    if values["internal_marks_pct"]<60: reasons.append("Internal assessment performance is relatively low.")
    if values["previous_gpa"]<7: reasons.append("Previous GPA is below 7.")
    if values["previous_backlogs"]>0: reasons.append("Previous backlog(s) increase academic risk.")
    if values["class_participation_pct"]<50: reasons.append("Class participation is relatively low.")
    if not reasons: reasons.append("No major rule-based risk indicators were detected.")
    return reasons
