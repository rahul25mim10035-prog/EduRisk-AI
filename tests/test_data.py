from src.data_loader import load_data
from src.data_validation import validate_data

def test_dataset():
    df=load_data()
    assert len(df)>=100
    assert validate_data(df)
