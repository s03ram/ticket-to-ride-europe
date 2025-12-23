from uuid import UUID, uuid4
from typing import List
from pydantic import BaseModel, Field
from data.models.cards import TrainCard, DestinationTicket
from data.models.colors import TrainColor, PlayerColor
from data.models.route import Route


class Player(BaseModel):
    """Represents a player in the game"""
    id: UUID = Field(default_factory=uuid4)
    name: str
    train_cards: List[TrainCard] = Field(default_factory=list)
    destination_tickets: List[DestinationTicket] = Field(default_factory=list)
    trains_remaining: int = 45
    score: int = 0
    color: PlayerColor
