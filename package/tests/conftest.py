import pytest

from sklearn.model_selection import train_test_split
from classification_model.config.core import config
from classification_model.processing.data_manager import load_dataset


@pytest.fixture()
def sample_input_data():
    """
    @pytest.fixture() is a decorator for this function,
    essentially telling pytest that this function provides a resource
    that can be used by other test functions.

    The return value test_data is used when sample_input_data is used as an argument
    in another function.

    This function sample_input_data is used in test_features.py for assertion.
    """
    data = load_dataset(file_name=config.app_config.training_data_file) 
    # data is a preprocessed dataframe. 
    # see ../classification_model/processing/data_manager, load_dataset function
    X_train, X_test, y_train, y_test = train_test_split(
        data,  # return features + target as X_test
        data[config.model_config.target],
        test_size=config.model_config.test_size,
        random_state=config.model_config.random_state,
    )
    test_data = X_test
    
    return test_data
