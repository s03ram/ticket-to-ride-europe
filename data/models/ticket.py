from pydantic import BaseModel
from typing import Literal
from data.models.city import City


class TicketModel(BaseModel):
    city_a: City
    city_b: City
    value: int
    length: Literal["short", "long"]
