from pydantic import BaseModel, field_validator
from data.cities import CITIES


class CityModel(BaseModel):
    name: str

    @field_validator("name", mode="after")
    @classmethod
    def validate_name(cls, value: str) -> None:
        if value.capitalize() not in CITIES:
            raise ValueError(f"Invalid city name: {value}")
