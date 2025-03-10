from random import shuffle
from typing import List
from components.cards import Card, TrainCard, DestinationCard, TrainColor


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []
        self.discard_pile: List[Card] = []

    def shuffle(self) -> None:
        shuffle(self.cards)

    def draw(self) -> Card:
        """Draw a card from the deck"""
        # draw pile is empty
        if not self.cards and self.discard_pile:
            self.cards = self.discard_pile
            self.discard_pile = []
            self.shuffle()
        return self.cards.pop() if self.cards else None

    def discard(self, card: Card):
        """Discard a card to the discard pile"""
        self.discard_pile.append(card)


class TrainDeck(Deck):
    """Specific deck for train cards"""
    def __init__(self):
        super().__init__()
        self._initialize_deck()

    def _initialize_deck(self):
        # Add regular train cards (12 of each color)
        card_id = 0
        for color in TrainColor:
            if color != TrainColor.LOCOMOTIVE:
                for _ in range(12):
                    self.cards.append(TrainCard(card_id, color))
                    card_id += 1

        # Add 14 locomotive (wild) cards
        for _ in range(14):
            self.cards.append(TrainCard(card_id, TrainColor.LOCOMOTIVE))
            card_id += 1

        self.shuffle()


class DestinationDeck(Deck):
    """Specific deck for destination tickets"""
    def __init__(self, destinations: List[tuple]):
        super().__init__()
        self._initialize_deck(destinations)

    def _initialize_deck(self, destinations: List[tuple]):
        # destinations should be a list of tuples: (city_from, city_to, points)
        for i, (city_from, city_to, points) in enumerate(destinations):
            self.cards.append(DestinationCard(i, city_from, city_to, points))
        self.shuffle()
