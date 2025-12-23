from typing import List, Optional
from data.models.cards import TrainCard, DestinationTicket
from data.models.colors import TrainColor


class TrainCardDeck:
    """Manages the train card deck, discard pile, and face-up cards"""
    
    def __init__(self):
        self.draw_pile: List[TrainCard] = []
        self.discard_pile: List[TrainCard] = []
        self.face_up_cards: List[TrainCard] = []
        
    def initialize_deck(self):
        """Create a standard Ticket to Ride deck"""
        cards = []
        
        for color in TrainColor:
            if color == TrainColor.LOCOMOTIVE:
                count = 14  # 14 locomotive cards
            else:
                count = 12  # 12 of each other color
            
            for _ in range(count):
                cards.append(TrainCard(color=color))
        
        self.draw_pile = cards
        self.shuffle()
        
        # Draw 5 face-up cards
        self.face_up_cards = [self.draw_pile.pop() for _ in range(5)]
    
    def shuffle(self):
        """Shuffle the draw pile"""
        import random
        random.shuffle(self.draw_pile)
    
    def draw_card(self) -> Optional[TrainCard]:
        """Draw a card from the deck"""
        if not self.draw_pile:
            # Reshuffle discard pile if draw pile is empty
            if self.discard_pile:
                self.draw_pile = self.discard_pile
                self.discard_pile = []
                self.shuffle()
            else:
                raise ValueError("No cards in the pile neither in the discard.")
        
        return self.draw_pile.pop()
    
    def replace_face_up_card(self, index: int) -> Optional[TrainCard]:
        """Replace a face-up card that was taken"""
        if 0 <= index < len(self.face_up_cards):
            new_card = self.draw_card()
            if new_card:
                old_card = self.face_up_cards[index]
                self.face_up_cards[index] = new_card
                return old_card
        raise IndexError("Invalid face-up card index.")
    
    def check_too_many_locomotives(self) -> bool:
        """Check if 3+ face-up cards are locomotives"""
        locomotive_count = sum(
            1 for card in self.face_up_cards 
            if card.color == TrainColor.LOCOMOTIVE
        )
        return locomotive_count >= 3
    
    def refresh_face_up_cards(self):
        """Discard and redraw all face-up cards"""
        self.discard_pile.extend(self.face_up_cards)
        self.face_up_cards = [self.draw_card() for _ in range(5)]


class DestinationTicketDeck:
    """Manages the destination ticket deck"""
    
    def __init__(self):
        self.draw_pile: List[DestinationTicket] = []
        self.discard_pile: List[DestinationTicket] = []
    
    def initialize_deck(self, tickets: List[DestinationTicket]):
        """Initialize with a set of destination tickets"""
        self.draw_pile = tickets
        self.shuffle()
    
    def shuffle(self):
        """Shuffle the draw pile"""
        import random
        random.shuffle(self.draw_pile)
    
    def draw_tickets(self, count: int) -> List[DestinationTicket]:
        """Draw multiple tickets"""
        drawn = []
        for _ in range(min(count, len(self.draw_pile))):
            drawn.append(self.draw_pile.pop())
        return drawn

    def discard_tickets(self, tickets: List[DestinationTicket]):
        """Discard destination tickets"""
        self.discard_pile.extend(tickets)
        
    def reinit_deck(self) -> None:
        """Reinitialize deck with discard pile"""
        self.initialize_deck(self.discard_pile)
        self.discard_pile: List[DestinationTicket] = []
