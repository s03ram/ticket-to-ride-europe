from components.cards import Card, TrainCard, DestinationCard


class Player:
    """
    The Player class tracks a player's name, color,
    train cards, ticket cards, remaining train pieces and score.

    Attributes:
        color (str): The player's chosen color
        train_cards (list): The player's current train cards
        destination_cards (list): The player's current ticket cards
        train_pieces (int): Number of train pieces remaining, starts at 45
        score (int): The player's current score
    """
    def __init__(self, color):
        self.color = color
        self.train_cards = []
        self.destination_cards = []
        self.train_pieces = 45
        self.stations = 3
        self.score = 0

    def add_card(self, card: Card):
        """Add a card in the convenient hand"""
        if isinstance(card, TrainCard):
            self.train_cards.append(card)
        elif isinstance(card, DestinationCard):
            self.destination_cards.append(card)
        else:
            raise ValueError("Invalid card type")

    def __str__(self):
        """Return a string representation of the player"""
        train_cards_str = ', '.join(
            str(card) for card in self.train_cards
            )
        destination_cards_str = ', '.join(
            str(card) for card in self.destination_cards
            )
        return (f"Player {self.color}:\n"
                f"  Score: {self.score}\n"
                f"  Train Pieces: {self.train_pieces}\n"
                f"  Station Pieces: {self.stations}\n"
                f"  Train Cards: {train_cards_str}\n"
                f"  Destination Cards: {destination_cards_str}\n"
                )
