import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from src.config import FEATURES,TARGET,MODEL_PATH,RESULTS_PATH
from src.data_loader import load_data
from src.data_validation import validate_data
from src.preprocessing import build_preprocessor
from src.model_training import build_models
from src.model_comparison import compare_models

def main():
    df=load_data()
    validate_data(df)
    X=df[FEATURES]; y=df[TARGET]
    X_train,X_test,y_train,y_test=train_test_split(
        X,y,test_size=.2,random_state=42,stratify=y
    )
    models=build_models(build_preprocessor())
    results,fitted=compare_models(models,X_train,X_test,y_train,y_test)
    results_df=pd.DataFrame(results).sort_values("F1 Score",ascending=False)
    best_name=results_df.iloc[0]["Model"]
    joblib.dump(fitted[best_name],MODEL_PATH)
    results_df.to_csv(RESULTS_PATH,index=False)
    print(results_df.to_string(index=False))
    print(f"Selected model: {best_name}")
    print(f"Saved model: {MODEL_PATH}")

if __name__=="__main__":
    main()
