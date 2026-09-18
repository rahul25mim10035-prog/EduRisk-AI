# Process Workflow

```mermaid
flowchart TD
    A[Start] --> B[Enter Student Indicators]
    B --> C{Are Inputs Valid?}
    C -- No --> D[Show Error Message]
    D --> B
    C -- Yes --> E[Load Trained Model]
    E --> F[Preprocess Input]
    F --> G[Predict Risk Category]
    G --> H[Calculate Prediction Probabilities]
    H --> I[Check Rule-based Indicators]
    I --> J[Generate Intervention Suggestions]
    J --> K[Display Terminal Result]
    K --> L[End]
```

## Training Workflow

```text
CSV dataset
   ↓
Validation
   ↓
80:20 stratified split
   ↓
Preprocessing
   ↓
Logistic Regression + Random Forest + Gradient Boosting
   ↓
Metric comparison
   ↓
Select highest weighted F1 Score
   ↓
Save trained pipeline
```
