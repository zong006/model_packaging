Assignment Task for Section05 of "Deployment of Machine Learning Models" on Udemy.
Link: https://www.udemy.com/course/deployment-of-machine-learning-models/?couponCode=KEEPLEARNING


# File/Directory Descriptions (WIP)

## 1. package
Contains and organizes the files for model packaging into PyPI. 
- tox.ini
- build files
- ML model training 
- ML model evaluation

#### Classification Model Pipeline
- import data -> classification_model/processing/data_manager.py
- pre-processing features -> classification_model/processing/data_manager.py
- train-test split -> classification_model/train_pipeline.py
- data imputation/feature transformation -> classification_model/pipeline.py
- scaling the data -> classification_model/pipeline.py
- fit the model -> classification_model/pipeline.py
- evaluate model -> tests/test_prediction.py

#### Build files:
- MANIFEST.in (specify files to be included/excluded)
- setup.py (specify metadata of package)
- pyproject.toml

#### To Retrain A Model And Update The Package
- go to classification_model/VERSION and update the version number. 
- run tox -e train. This runs the training pipeline and saves an updated model in a .pkl file with the 
new version number according to classification_model/VERSION
- clear the build cache by running rm -rf build dist *.egg-info
- upload to PyPI: 
    - python setup.py sdist bdist_wheel
    - twine upload dist/*


## 2. classification_api




# First Trial Run
- run "tox -e train" from the package directory. This trains up a model and saves the pipeline into a .pkl file under "classification_model/trained_models"
- go to the package directory and run "pip install .". This treats the package folder containing setup.py and MANIFEST.in as a package to be installed and used in scripts.
- run "python main.py", where a sample input is a .csv file with a single row having same features as the raw dataset. This file is loaded and fed into the persisted pipeline, producing an output.
- More thorough handling of missing values have to be considered.





