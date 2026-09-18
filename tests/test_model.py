from src.predictor import load_model

def test_model_exists():
    assert load_model() is not None
