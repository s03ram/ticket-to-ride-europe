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
    
    def has_cards_for_route(self, route: Route) -> str | bool:
        """Check if player has enough cards to claim a route"""
        locomotive_count = sum(1 for card in self.train_cards if card.color == TrainColor.LOCOMOTIVE)
        if route.color is None:
            color_counts = {}
            for card in self.train_cards:
                color_counts[card.color] = color_counts.get(card.color, 0) + 1
            
            # Check if any color (including locomotives) has enough cards
            for color, count in color_counts.items():
                if color != TrainColor.LOCOMOTIVE and count + locomotive_count >= route.length:
                    return color
                elif color == TrainColor.LOCOMOTIVE and count >= route.length:
                    return color
            return False
        else:
            # Colored route - need that color + locomotives
            color_count = (1 for card in self.train_cards if card.color == route.color)
            return route.color if color_count + locomotive_count >= route.length else False

    def can_claim_route(self, route: Route) -> str | bool:
        """Check if player can claim a route"""
        if route.is_claimed():
            return False
        elif self.trains_remaining < route.length:
            return False
        else:
            return self.has_cards_for_route(route)
