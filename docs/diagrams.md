# UML / Design Diagrams

## Use Case Diagram

```mermaid
flowchart LR
    S((Student)) --> A[Enter Student Indicators]
    S --> B[View Risk Prediction]
    S --> C[View Intervention Suggestions]
    M((Faculty Mentor)) --> B
    M --> C
    AD((Project Administrator)) --> D[Train and Evaluate Models]
```

## Component Diagram

```mermaid
flowchart TD
    CLI[Terminal Interface] --> P[Prediction Module]
    UI[Optional Streamlit Interface] --> P
    P --> ML[Saved ML Pipeline]
    P --> X[Rule-based Indicator Module]
    P --> R[Intervention Module]
    T[Training Pipeline] --> ML
    D[CSV Dataset] --> T
```

## Sequence Diagram

```mermaid
sequenceDiagram
    actor User
    participant CLI as Terminal Interface
    participant P as Predictor
    participant M as ML Model
    participant X as Indicator Module
    participant R as Intervention Module

    User->>CLI: Enter student indicators
    CLI->>P: Send validated features
    P->>M: Predict risk
    M-->>P: Risk + probabilities
    P->>X: Check predefined indicators
    X-->>P: Key indicators
    P->>R: Generate suggestions
    R-->>P: Recommendations
    P-->>CLI: Return complete result
    CLI-->>User: Display prediction and guidance
```

## Storage Design

The prototype uses a CSV file for the demonstration dataset and a local serialized model file for the trained pipeline. A relational database is not required for the current scope, so an ER diagram is not applicable.
