import utils4test
utils4test.load_path()
from src.biomodels_restful_api_client import services


def test_get_model_info():
    model_id = "BIOMD0000000200"
    assert model_id == services.get_model_info(model_id)
