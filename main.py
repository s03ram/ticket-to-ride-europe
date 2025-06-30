import os

from random import shuffle
from components.board import Board
from components.player import Player
from data.board_data import PLAYERS_COLORS
from components.deck import Deck

class Game:
    def __init__(self) -> None:
        self.players = list(self.init_players(2))  # Initialize with 2 players for now
    
    def init_players(self, players: int):
        """
        Initialize players based on the number of players.
        """
        for i in range(players):
            yield Player(
                id=i,
                name=f"Player {i + 1}",
                color=PLAYERS_COLORS[i],
                trains_deck=Deck(),
                tickets_deck=Deck(),
            )


    def check_trains_offer(self) -> None:
        """Check train offer conditions :
            - = 5 cards in the offer
            - no more than 2 locomotives
        """
        self.fill_trains_offer()
        while self.too_much_locomotives():
            for card in self.trains_offer.get_cards():
                self.trains_draw.add_card(self.trains_offer.remove_card(card)) # type: ignore
    
    def fill_trains_offer(self) -> None:
        """Fill the trains offer with cards from the draw deck
        """
        while len(self.trains_offer.get_cards()) < 5:
            self.trains_offer.add_card(self.trains_draw.get_card())
    
    def too_much_locomotives(self) -> bool:
        """Check if there are too many locomotives in the trains offer
        """
        loco_count = sum(1 for card in self.trains_offer.get_cards() if card.color == "locomotive") # type: ignore
        return loco_count >= 3