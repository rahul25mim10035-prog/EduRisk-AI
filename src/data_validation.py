from .config import FEATURES, TARGET

def validate_data(df):
    required=set(FEATURES+["student_id",TARGET])
    missing=required-set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    if df[FEATURES].isnull().any().any():
        raise ValueError("Feature columns contain missing values.")
    if not set(df[TARGET].unique()).issubset({"Low","Medium","High"}):
        raise ValueError("Unexpected risk labels.")
    return True
