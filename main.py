from package.classification_model import predict
from package.classification_model.processing import data_manager


file_path = "testing.csv"

input_ = data_manager.load_dataset(file_name=file_path)

results = predict.make_prediction(input_data=input_)
print(results)
