# Requirements Specification

## 1. Objectives

1. Build a complete supervised machine-learning workflow for academic risk classification.
2. Use student performance indicators as input features.
3. Compare multiple classification models using standard evaluation metrics.
4. Produce a clear risk prediction for a new student record.
5. Add simple interpretation and intervention suggestions around the prediction.

## 2. Functional Requirements

### FR1 – Data Loading
The system shall load student performance records from the CSV dataset.

### FR2 – Data Validation
The system shall check that required columns and supported risk labels are present before training.

### FR3 – Data Preprocessing
The system shall preprocess numeric features using missing-value handling and standardization.

### FR4 – Model Training and Comparison
The system shall train Logistic Regression, Random Forest, and Gradient Boosting models and compare their performance.

### FR5 – Academic Risk Prediction
The system shall accept the required student indicators and classify the student as Low, Medium, or High risk.

### FR6 – Probability Display
The system shall display the prediction probability for each available risk class.

### FR7 – Indicator Interpretation
The system shall identify predefined academic indicators that may require attention.

### FR8 – Intervention Suggestions
The system shall provide simple suggestions based on the input indicators and predicted risk.

## 3. Non-Functional Requirements

### NFR1 – Usability
The terminal interface shall use clear prompts and structured output.

### NFR2 – Reliability
The application shall validate input ranges and provide a clear message when the trained model is unavailable.

### NFR3 – Maintainability
The implementation shall keep data, preprocessing, training, prediction, explanation, and intervention logic in separate modules.

### NFR4 – Performance
A single student prediction shall complete quickly on a normal personal computer after the model has been trained.

### NFR5 – Error Handling
Invalid values shall not be silently accepted; the user shall be asked to enter a valid value.

### NFR6 – Resource Efficiency
The prototype shall use a lightweight CSV dataset and local model files so that it can run without a server.
