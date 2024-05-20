import numpy as np
import pandas as pd
from fastapi.testclient import TestClient
from sklearn.metrics import accuracy_score


def test_make_prediction(client: TestClient, test_data: pd.DataFrame):
    """
    The argument sample_input_data is a fixture from conftest.py,
    where the return value of sample_input_data is test_data 
    i.e., treat sample_input_data logically as test_data.
    """
    
    # Given
    payload = {
        # ensure pydantic plays well with np.nan
        "inputs": test_data.replace({np.nan: None}).to_dict(orient="records")
    }
    
    # When
    response = client.post(
        "http://localhost:8002/api/v1/predict",
        json=payload,
    )
    print(response.json())  
    
    # Then
    assert response.status_code == 200
    prediction_data = response.json()
    assert prediction_data["predictions"]
    assert prediction_data["errors"] is None

    y_test = test_data["Survived"]
    accuracy = accuracy_score(y_test, prediction_data["predictions"])
    assert accuracy > 0.75
