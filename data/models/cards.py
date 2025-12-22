from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from data.models.colors import TrainColor

class TrainCard(BaseModel):
    """Represents a single train card"""
    id: UUID = Field(default_factory=uuid4)
    color: TrainColor
    
    class Config:
        frozen = True 


class DestinationTicket(BaseModel):
    """Represents a destination ticket connecting two cities"""
    id: UUID = Field(default_factory=uuid4)
    city1: str
    city2: str
    points: int
    
    class Config:
        frozen = True