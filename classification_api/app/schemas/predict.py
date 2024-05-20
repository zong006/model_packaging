from typing import List, Optional, Any
from pydantic import BaseModel
from classification_model.processing.validation import PassengerDataInputSchema

class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[int]]

class MultiplePassengerDataInputs(BaseModel):
    inputs: List[PassengerDataInputSchema]  

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "PassengerId": 1,
                        "Pclass": 3,
                        "Name": "Braund, Mr. Owen Harris",
                        "Sex": "male",
                        "Age": 22,
                        "SibSp": 1,
                        "Parch": 0,
                        "Ticket": "A/5 21171",
                        "Fare": 7.25,
                        "Cabin": "?",
                        "Embarked": "S"
                    }
                ]
            }
        }
