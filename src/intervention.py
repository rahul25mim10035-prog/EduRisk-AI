def recommendations(values,risk):
    rec=[]
    if values["attendance_pct"]<75: rec.append("Improve attendance and review missed topics.")
    if values["study_hours_per_day"]<2: rec.append("Create a consistent daily study schedule.")
    if values["assignment_score_pct"]<60: rec.append("Complete assignments earlier and review feedback.")
    if values["internal_marks_pct"]<60: rec.append("Revise internal-assessment topics and practice questions.")
    if values["previous_backlogs"]>0: rec.append("Create a weekly plan for pending subjects.")
    if risk=="High": rec.append("Discuss an academic support plan with a faculty mentor.")
    elif risk=="Medium": rec.append("Monitor progress weekly and focus on weak indicators.")
    else: rec.append("Maintain current habits and review performance periodically.")
    return list(dict.fromkeys(rec))
