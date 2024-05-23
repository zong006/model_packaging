# File/Directory Descriptions (WIP)

## 1. package 
Assignment Task for Section05 of "Deployment of Machine Learning Models" on Udemy.
Link: https://www.udemy.com/course/deployment-of-machine-learning-models/?couponCode=KEEPLEARNING
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
- run "tox -e train". This runs the training pipeline and saves an updated model in a .pkl file with the 
new version number according to classification_model/VERSION
- clear the build cache by running "rm -rf build dist *.egg-info"
- upload to PyPI: 
    - "python -m build"
    - "twine upload dist/*"

#### To Evaluate The Model
- run "tox -e test_package". This evaluates if the model is working as intended as well as the accuracy using 
sklearn classification metrics.

#### First Trial Run
- run "tox -e train" from the package directory. This trains up a model and saves the pipeline into a .pkl file under "classification_model/trained_models"
- go to the package directory and run "pip install .". This treats the package folder containing setup.py and MANIFEST.in as a package to be installed and used in scripts.
- run "python main.py", where a sample input is a .csv file with a single row having same features as the raw dataset. This file is loaded and fed into the persisted pipeline, producing an output.
- More thorough handling of missing values have to be considered, but the package works as intended.

## 2. classification_api
A simple interface for now, with two API endpoints:
- /predict
- /health
Other files include
- tox.ini
- Procfile

#### API's
- /health shows if the server is functioning properly.
- /predict uses the make_prediction function from the classification_model package which takes in raw inputs 
and returns a prediction.

#### Running and Testing the API
- Running:
    - run "tox -e run run" which starts up the local server at localhost:8002. 
- Testing
    - run "tox -e test_app". This checks if the model is producing valid outputs, and if it is still accurate. Similar to 
    test_package function in the packaging phase.

#### Procfile
Tells the deployment platform to start a web server using Uvicorn, serving the application defined in app.main:app, and to listen on all network interfaces at the port specified by the environment variable $PORT. 

#### Testing The Deployment
A simple test deployment will be via Railway 
- railway init -> railway link -> railway up
- go to Settings of the project (not of the service), generate the web domain and go to the url. Use it as per running the API with tox.


## 3. CI/CD via Github Actions
The process so far has been manual. Whenever there is an update such as retraining a model, or any updates to the api or package, commands have to be run manually. Now, the task is to automate these processes such that whenever there are changes pushed to github, or new tags are released, the following pipeline is activated:
- a process to run tests are triggered. This checks if the changes made will cause the code to break.
- deployment to railway is triggered automatically.
These can be done through Github actions by including a workflow .yml file. Keys from railway also have to be added as environment variables to the Github repo.

#### Workflows .yml File
There are two workflow files specifying jobs to be triggered by:
- pushing to Github. This will be in-between versions to check if any changes breaks the code. 
    - triggers jobs defined in push.yml: test the app api -> deploy to railway
- releasing a new version tag. Set it to happen when a new tag is released. For clarity, do the following:
    - create a new branch "update_pkg_version"
    -  increment the version number manually under package/classification_model/VERSION
    - push changes to github 
    - release a new tag with version number according to the package/classification_model/VERSION file
        - triggers jobs defined in update_package.yml: build package -> publish to PyPI 
    - lastly, (manual for now) train a new model with "tox -e train" and push the new trained model under package/classification_model/trained_models to Github. Then do a pull request to the master branch to merge it back. 

