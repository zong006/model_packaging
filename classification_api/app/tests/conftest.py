import pytest
from typing import Generator
from fastapi.testclient import TestClient

from sklearn.model_selection import train_test_split
from classification_model.config.core import config
from classification_model.processing.data_manager import load_dataset

from app.main import app

@pytest.fixture()
def test_data():
    data = load_dataset(file_name=config.app_config.training_data_file) 
    # see classification_model/processing/data_manager, load_dataset function
    X_train, X_test, y_train, y_test = train_test_split(
        data,  # return features + target as X_test
        data[config.model_config.target],
        test_size=config.model_config.test_size,
        random_state=config.model_config.random_state,
    )
    return X_test

@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides = {}
