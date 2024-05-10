from classification_model.config.core import config
from classification_model.processing.features import ExtractLetterTransformer


def test_extract_letter_transformer(sample_input_data):
    """
    The argument sample_input_data is a fixture from conftest.py,
    where the return value of sample_input_data is train_data 
    i.e., treat sample_input_data logically as train_data.
    """
    # Given
    transformer = ExtractLetterTransformer(
        variables=config.model_config.cabin
    )
    
    assert sample_input_data["Cabin"].iat[3] == "B78"

    # When
    subject = transformer.fit_transform(sample_input_data)

    # Then
    assert subject["Cabin"].iat[3] == "B"
