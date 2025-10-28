from pydantic import BaseModel
from typing import Literal
from data.models.city import CityModel


class TicketModel(BaseModel):
    city_a: CityModel
    city_b: CityModel
    value: int
    length: Literal["short", "long"]
