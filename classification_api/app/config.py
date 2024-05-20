from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    # # Meta
    # logging: LoggingSettings = LoggingSettings()

    PROJECT_NAME: str = "Titanic Survival Prediction API"


settings = Settings()


