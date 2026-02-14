from enum import Enum


class GamePhase(str, Enum):
    """Current phase of the game"""

    SETUP = "setup"
    PLAYING = "playing"
    FINAL_ROUND = "final_round"
    ENDED = "ended"


class PlayerAction(str, Enum):
    """Possible actions a player can take"""

    DRAW_TRAIN_CARDS = "draw_train_cards"
    CLAIM_ROUTE = "claim_route"
    CLAIM_STATION = "claim_station"
    DRAW_DESTINATION_TICKETS = "draw_destination_tickets"
