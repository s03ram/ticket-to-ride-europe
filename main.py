from random import shuffle
from components.board import Board
from components.player import Player
from data.board_data import PLAYERS_COLORS
from components.deck import Deck

class Game:
    def __init__(self) -> None:
        self.players = list(self.__init_players(2))  # Initialize with 2 players for now
        self.__init_board()


    def __init_players(self, players: int):
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


    def __init_board(self) -> None:
        """Initialize the game board
        """
        self.board = Board()
        self.check_trains_offer()


    def check_trains_offer(self) -> None:
        """Check train offer conditions :
            - = 5 cards in the offer
            - no more than 2 locomotives
        """
        self.__fill_trains_offer()
        while self.__too_much_locomotives():
            self.__empty_trains_offer()
            self.__fill_trains_offer()
        self.board.trains_offer.shuffle()


    def __fill_trains_offer(self) -> None:
        """Fill the trains offer with cards from the draw deck
        """
        while len(self.board.trains_offer.get_cards()) < 5:
            self.board.trains_offer.add_card(self.board.trains_draw.get_card())


    def __empty_trains_offer(self) -> None:
        """Empty the train offer and put the cards back in the draw deck
        """
        for card in self.board.trains_offer.get_cards():
            self.board.trains_draw.add_card(card)
        self.board.trains_draw.shuffle()
        self.board.trains_offer = Deck()


    def __too_much_locomotives(self) -> bool:
        """Check if there are too many locomotives in the trains offer
        """
        loco_count = sum(1 for card in self.board.trains_offer.get_cards() if getattr(card, "color", None) == "locomotive")
        return loco_count >= 3







if __name__ == "__main__":
    game = Game()
    game.board.show()
    print("Trains offer:", game.board.trains_offer)
