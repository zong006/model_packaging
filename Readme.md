Assignment Task for Section05 of "Deployment of Machine Learning Models" on Udemy.
Link: https://www.udemy.com/course/deployment-of-machine-learning-models/?couponCode=KEEPLEARNING


File/Folder Descriptions (WIP)

Classification Model Pipeline
- import data -> classification_model/processing/data_manager.py
- pre-processing features -> classification_model/processing/data_manager.py
- train-test split -> classification_model/train_pipeline.py
- data imputation/feature transformation -> classification_model/pipeline.py
- scaling the data -> classification_model/pipeline.py
- fit the model -> classification_model/pipeline.py
- evaluate model -> tests/test_prediction.py


Build files:
- MANIFEST.in (specify files to be included/excluded)
- setup.py (specify metadata of package)
- pyproject.toml

First Trial Run
- run "tox -e train" from the package directory. This trains up a model and saves the pipeline into a .pkl file under "classification_model/trained_models"
- go to the package directory and run "pip install .". This treats the package folder containing setup.py and MANIFEST.in as a package to be installed and used in scripts.
- run "python main.py", where a sample input is a .csv file with a single row having same features as the raw dataset. This file is loaded and fed into the persisted pipeline, producing an output.
