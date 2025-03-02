from enum import Enum
from dataclasses import dataclass


class TrainColor(Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
    YELLOW = "yellow"
    BLACK = "black"
    WHITE = "white"
    ORANGE = "orange"
    PINK = "pink"
    LOCOMOTIVE = "locomotive"  # Wild card


@dataclass
class City:
    name: str
    country: str


class Card:
    """Base abstract class for all cards"""
    def __init__(self, card_id: int):
        self.card_id = card_id


class TrainCard(Card):
    """Train cards used to claim routes"""
    def __init__(self, card_id: int, color: TrainColor):
        super().__init__(card_id)
        self.color = color

    def __str__(self):
        return f"Train Card ({self.color.value})"


class DestinationCard(Card):
    """Destination tickets connecting two cities"""
    def __init__(
            self, card_id: int, city_from: City, city_to: City, points: int
            ):
        super().__init__(card_id)
        self.city_from = city_from
        self.city_to = city_to
        self.points = points
        self.completed = False

    def __str__(self):
        return (f"{self.city_from.name} <-> {self.city_to.name}"
                f"({self.points} pts)")
