from enum import Enum


class TrainColor(str, Enum):
    """Train card colors in Ticket to Ride"""

    RED = "red"
    BLUE = "blue"
    GREEN = "green"
    YELLOW = "yellow"
    ORANGE = "orange"
    BLACK = "black"
    WHITE = "white"
    PINK = "pink"
    LOCOMOTIVE = "locomotive"


class PlayerColor(str, Enum):
    """Player colors in Ticket to Ride"""

    RED = "red"
    BLUE = "blue"
    GREEN = "green"
    YELLOW = "yellow"
    BLACK = "black"
