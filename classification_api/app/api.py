import json
from typing import Any
import pandas as pd
import numpy as np
from loguru import logger
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from classification_model import __version__ as model_version
from classification_model.predict import make_prediction
from app.config import settings
from app import __version__, schemas

api_router = APIRouter()

@api_router.get("/health", response_model=schemas.Health, status_code=200)
def health() -> dict:
    health = schemas.Health(
        name=settings.PROJECT_NAME, api_version=__version__, model_version=model_version
    )
    return health.dict()

@api_router.post("/predict", response_model=schemas.PredictionResults, status_code=200)
def predict(input_data: schemas.MultiplePassengerDataInputs) -> Any:
    try:
        # Ensure input data is properly formatted
        input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid input data format: {e}")

    logger.info(f"Making prediction on inputs: {input_data.inputs}")
    
    results = make_prediction(input_data=input_df.replace({np.nan: None}))

    if not isinstance(results['predictions'].tolist(), list):
        logger.error("Predictions field is not a list")
        raise HTTPException(status_code=500, detail="Internal Server Errorrrrrrr")
    
    if results["errors"] is not None:
        logger.warning(f"Prediction validation error: {results.get('errors')}")
        raise HTTPException(status_code=400, detail=json.loads(results["errors"]))

    logger.info(f"Prediction results: {results.get('predictions')}")

    # prediction results is an array instead of a list. 
    # must be converted to a list for test_api
    pred_list = results['predictions'].tolist()
    results['predictions'] = pred_list

    return results


