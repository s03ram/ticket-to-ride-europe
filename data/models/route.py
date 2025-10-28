from pydantic import BaseModel, field_validator
from data.models.city import CityModel
from data.colors import TRAIN_COLORS


class RouteModel(BaseModel):
    city_a: CityModel
    city_b: CityModel
    length: int
    color: str | bool
    locomotive: int
    tunnel: bool

    @field_validator("color", mode="after")
    @classmethod
    def validate_color(cls, value: str | bool) -> None:
        if value not in TRAIN_COLORS:
            raise ValueError(f"Invalid train color: {value}")
