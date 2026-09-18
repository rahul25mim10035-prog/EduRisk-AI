import streamlit as st
from src.predictor import load_model,predict_student
from src.explainability import explain
from src.intervention import recommendations

st.set_page_config(page_title="EduRisk AI",page_icon="🎓",layout="wide")
st.title("🎓 EduRisk AI")
st.caption("Explainable Student Academic Risk Prediction & Intervention System")

@st.cache_resource
def get_model():
    return load_model()

try:
    model=get_model()
except Exception:
    st.error("Model not found. Run `python train.py` first.")
    st.stop()

with st.sidebar:
    st.header("Student Inputs")
    attendance=st.slider("Attendance (%)",0.0,100.0,80.0)
    study=st.slider("Study hours/day",0.0,12.0,3.0)
    assignment=st.slider("Assignment score (%)",0.0,100.0,75.0)
    internal=st.slider("Internal marks (%)",0.0,100.0,70.0)
    gpa=st.slider("Previous GPA",0.0,10.0,7.5)
    backlogs=st.number_input("Previous backlogs",0,10,0)
    sleep=st.slider("Sleep hours/day",0.0,12.0,7.0)
    participation=st.slider("Class participation (%)",0.0,100.0,70.0)

values={
"attendance_pct":attendance,"study_hours_per_day":study,
"assignment_score_pct":assignment,"internal_marks_pct":internal,
"previous_gpa":gpa,"previous_backlogs":backlogs,
"sleep_hours":sleep,"class_participation_pct":participation
}

if st.button("Predict Academic Risk",type="primary"):
    risk,prob=predict_student(model,values)
    st.subheader(f"Predicted Risk: {risk}")
    if prob:
        st.write("Prediction probabilities")
        st.bar_chart(prob)
    c1,c2=st.columns(2)
    with c1:
        st.markdown("### 🔎 Key Indicators")
        for item in explain(values): st.write("•",item)
    with c2:
        st.markdown("### 💡 Suggested Intervention")
        for item in recommendations(values,risk): st.write("•",item)
