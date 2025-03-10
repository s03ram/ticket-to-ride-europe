from typing import List, Optional
from enum import Enum
from components.cards import TrainCard, TrainColor
from components.decks import TrainDeck
from components.players import Player


class DrawError(Exception):
    """Custom exception for drawing errors"""
    ...


class DrawPhase(Enum):
    """Track the drawing phase of a player's turn"""
    NOT_DRAWING = 0
    FIRST_CARD = 1
    SECOND_CARD = 2


class Game:
    def __init__(self):
        self.train_deck = TrainDeck()
        self.face_up_cards: List[TrainCard] = []
        self.draw_phase = DrawPhase.NOT_DRAWING

        # Initialize face-up cards
        self.face_up_cards = [self.train_deck.draw() for _ in range(5)]
        self._check_face_up_cards()

    def _check_face_up_cards(self):
        """Check if there are 3 or more locomotives face up"""
        locomotive_count = sum(
            1 for card in self.face_up_cards
            if card.color == TrainColor.LOCOMOTIVE
            )
        if locomotive_count >= 3:
            # Discard all cards and draw new ones
            for card in self.face_up_cards:
                self.train_deck.discard(card)
            self.face_up_cards = [self.train_deck.draw() for _ in range(5)]
            self._check_face_up_cards()  # Recursive check

    def draw_face_up_card(self, card_index: int) -> TrainCard:
        """Draw a face-up card"""
        if not 0 <= card_index < len(self.face_up_cards):
            raise DrawError("Invalid card index")

        selected_card = self.face_up_cards[card_index]

        # Can't draw a face-up locomotive as second card
        if (self.draw_phase == DrawPhase.FIRST_CARD and
                selected_card.color == TrainColor.LOCOMOTIVE):
            self.draw_phase = DrawPhase.SECOND_CARD

        elif (self.draw_phase == DrawPhase.SECOND_CARD and
                selected_card.color == TrainColor.LOCOMOTIVE):
            raise DrawError("Cannot draw a locomotive as second card")

        # Remove and replace the selected card
        self.face_up_cards[card_index] = self.train_deck.draw()
        self._check_face_up_cards()

        return selected_card

    def draw_from_deck(self) -> TrainCard:
        """Draw a card from the deck"""
        return self.train_deck.draw()


class GameController:
    """Handles game logic and player actions"""
    def __init__(self, players: List[Player]):
        self.game = Game()
        self.players = players
        self.current_player_index = 0
        self.draw_phase = DrawPhase.NOT_DRAWING

    def __init_players(self):
        """Initialize player hands"""
        for player in self.players:
            for _ in range(4):
                player.add_card(self.handle_card_draw(player))

    def handle_card_draw(
            self, player: Player,
            card_index: Optional[int] = None
            ) -> bool:
        """
        Handle a player's attempt to draw a card
        Returns True if the player's draw phase is complete

        Args:
            player (Player): The player drawing a card
            card_index (int, optional): The index of the face-up card to draw
        """
        try:
            if self.draw_phase == DrawPhase.NOT_DRAWING:
                self.draw_phase = DrawPhase.FIRST_CARD

            if card_index is not None:
                # Drawing face-up card
                card = self.game.draw_face_up_card(card_index)
            else:
                # Drawing from deck
                card = self.game.draw_from_deck()

            player.add_card(card)

            # Update draw phase
            if self.draw_phase == DrawPhase.FIRST_CARD:
                if (card.color == TrainColor.LOCOMOTIVE
                        and card_index is not None):
                    # If first card was a face-up locomotive, end draw phase
                    self.draw_phase = DrawPhase.NOT_DRAWING
                    return True
                self.draw_phase = DrawPhase.SECOND_CARD
                return False
            else:
                # Second card drawn, end draw phase
                self.draw_phase = DrawPhase.NOT_DRAWING
                return True

        except DrawError as e:
            print(f"Draw error: {e}")
            return False
