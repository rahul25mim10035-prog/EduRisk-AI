import joblib
import pandas as pd
from .config import MODEL_PATH,FEATURES

def load_model(path=MODEL_PATH):
    return joblib.load(path)

def predict_student(model,values):
    row=pd.DataFrame([values],columns=FEATURES)
    label=model.predict(row)[0]
    probabilities=model.predict_proba(row)[0] if hasattr(model,"predict_proba") else []
    classes=list(model.classes_) if hasattr(model,"classes_") else []
    return label,dict(zip(classes,probabilities))
