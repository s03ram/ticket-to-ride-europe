from typing import List
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from src.models.cards import DestinationTicket, TrainCard
from src.models.colors import PlayerColor


class Player(BaseModel):
    """Represents a player in the game"""

    id: UUID = Field(default_factory=uuid4)
    name: str
    train_cards: List[TrainCard] = Field(default_factory=list)
    destination_tickets: List[DestinationTicket] = Field(default_factory=list)
    trains_remaining: int = 45
    score: int = 0
    color: PlayerColor
