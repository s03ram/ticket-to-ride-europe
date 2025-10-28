from random import shuffle

from .card import TicketCard, TrainCard


class Deck:
    def __init__(self) -> None:
        self.cards: list[TicketCard|TrainCard] = []


    def __repr__(self) -> str:
        return f"Deck(cards=\n{self.cards})"


    def get_cards(self) -> list[TicketCard|TrainCard]:
        """Get the cards in the deck"""
        return self.cards


    def get_card(self) -> TicketCard|TrainCard:
        """Get a card from the deck"""
        return self.cards.pop(0)


    def get_card_by_id(self, id: int) -> TicketCard|TrainCard | None:
        """Get a card by its id"""
        for card in self.cards:
            if card.get_id() == id:
                return card
        return None


    def add_card(self, card: TicketCard|TrainCard) -> None:
        """Add a card to the deck"""
        self.cards.append(card)


    def remove_card(self, card: TicketCard|TrainCard) -> TicketCard|TrainCard | None:
        """Remove a card from the deck"""
        if card in self.cards:
            self.cards.remove(card)
            return card
        return None


    def shuffle(self) -> None:
        """Shuffle the deck"""
        shuffle(self.cards)

