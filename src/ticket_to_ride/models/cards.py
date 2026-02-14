from typing import Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from src.models.colors import TrainColor
from src.models.city import City


class TrainCard(BaseModel):
    """Represents a single train card"""

    id: UUID = Field(default_factory=uuid4)
    color: TrainColor

    class Config:
        frozen = True


class DestinationTicket(BaseModel):
    """Represents a destination ticket connecting two cities"""

    id: UUID = Field(default_factory=uuid4)
    city_a: City
    city_b: City
    points: int
    length: Literal["short", "long"]

    class Config:
        frozen = True
