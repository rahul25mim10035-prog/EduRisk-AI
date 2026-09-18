from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

def build_models(preprocessor):
    return {
        "Logistic Regression":Pipeline([
            ("preprocessor",preprocessor),
            ("classifier",LogisticRegression(max_iter=2000,random_state=42))
        ]),
        "Random Forest":Pipeline([
            ("preprocessor",preprocessor),
            ("classifier",RandomForestClassifier(
                n_estimators=250,random_state=42,class_weight="balanced"
            ))
        ]),
        "Gradient Boosting":Pipeline([
            ("preprocessor",preprocessor),
            ("classifier",GradientBoostingClassifier(random_state=42))
        ])
    }
