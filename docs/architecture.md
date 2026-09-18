# System Architecture

EduRisk AI is divided into a training pipeline and a prediction layer.

```mermaid
flowchart TD
    D[CSV Dataset] --> L[Data Loader]
    L --> V[Data Validation]
    V --> P[Preprocessing]
    P --> T[Model Training]
    T --> C[Model Comparison]
    C --> S[Selected Model]
    S --> M[Saved Model]

    U[Student Indicators] --> I[Input Validation]
    I --> Q[Prediction Module]
    M --> Q
    Q --> R[Risk + Probabilities]
    Q --> X[Rule-based Indicators]
    Q --> N[Intervention Suggestions]
    R --> O[Terminal Output]
    X --> O
    N --> O

    Q --> W[Optional Streamlit Dashboard]
    X --> W
    N --> W
```

## Main Components

- **Data Loader:** reads the CSV file.
- **Data Validation:** checks required fields and supported labels.
- **Preprocessing:** imputes missing numeric values and standardizes features.
- **Model Training:** creates the three supervised classifiers.
- **Model Comparison:** calculates Accuracy, Precision, Recall, and weighted F1 Score.
- **Predictor:** loads the selected model and predicts a new student's risk.
- **Explainability Layer:** applies predefined threshold rules to identify indicators for attention.
- **Intervention Layer:** converts identified indicators and risk level into suggestions.
- **Interfaces:** terminal CLI for direct output and optional Streamlit dashboard for visualization.
