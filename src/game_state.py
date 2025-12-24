from typing import Dict, List, Optional
from uuid import UUID

from src.board import Board
from src.models.deck import DestinationTicketDeck, TrainCardDeck
from src.models.game import GamePhase
from src.models.player import Player


class GameState:
    """Central game state manager"""

    def __init__(self, players: List[Player], board: Board):
        self.players: Dict[UUID, Player] = {p.id: p for p in players}
        self.board = board
        self.train_deck = TrainCardDeck()
        self.destination_deck = DestinationTicketDeck()
        self.current_player_index = 0
        self.player_order: List[UUID] = [p.id for p in players]
        self.phase = GamePhase.SETUP
        self.final_turn_triggered = False
        self.turn_count = 0

        # Track actions this turn
        self.actions_taken_this_turn = 0
        self.drew_locomotive_this_turn = False

    def get_current_player(self) -> Player:
        """Get the player whose turn it is"""
        player_id = self.player_order[self.current_player_index]
        return self.players[player_id]

    def get_player(self, player_id: UUID) -> Optional[Player]:
        """Get a player by ID"""
        return self.players.get(player_id)

    def next_turn(self):
        """Advance to the next player's turn"""
        self.current_player_index = (self.current_player_index + 1) % len(
            self.player_order
        )
        self.actions_taken_this_turn = 0
        self.drew_locomotive_this_turn = False
        self.turn_count += 1

        # Check if we should end the game
        if self.final_turn_triggered and self.turn_count % len(self.player_order) == 0:
            self.phase = GamePhase.ENDED
