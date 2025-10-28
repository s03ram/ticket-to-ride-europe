from .deck import Deck
from .card import TrainCard, TicketCard


class Player:
    def __init__(self, id: int, name: str, color: str, trains_deck: Deck, tickets_deck: Deck) -> None:
        """Represent a player"""
        self.id = id
        self.name = name
        self.color = color
        self.trains_deck = trains_deck
        self.tickets_deck = tickets_deck
        self.trains = 45
        self.stations = 3
        self.score = 0
        self.claimed_routes = []
        
    def get_id(self) -> int:
        """Get the player's ID"""
        return self.id
    
    def get_name(self) -> str:
        """Get the player's name"""
        return self.name
    
    def get_color(self) -> str:
        """Get the player's color"""
        return self.color
    
    def get_trains_deck(self) -> Deck:
        """Get the player's trains deck"""
        return self.trains_deck
    
    def add_train_to_deck(self, train: TrainCard) -> None:
        """Add a train to the player's trains deck"""
        self.trains_deck.add_card(train)
        
    def remove_train_from_deck(self, train: TrainCard) -> None:
        """Remove a train from the player's trains deck"""
        self.trains_deck.remove_card(train)
    
    def get_tickets_deck(self) -> Deck:
        """Get the player's tickets deck"""
        return self.tickets_deck
    
    def add_ticket_to_deck(self, ticket: TicketCard) -> None:
        """Add a ticket to the player's tickets deck"""
        self.tickets_deck.add_card(ticket)
        
    def remove_ticket_from_deck(self, ticket: TicketCard) -> None:
        """Remove a ticket from the player's tickets deck"""
        self.tickets_deck.remove_card(ticket)
    
    def get_remaining_trains(self) -> int:
        """Get the number of trains the player has left"""
        return self.trains
    
    def remove_train(self) -> None:
        """Remove a train from the player's count"""
        if self.trains > 0:
            self.trains -= 1
        else:
            raise ValueError("No trains left to remove")
    
    def get_remaining_stations(self) -> int:
        """Get the number of stations the player has left"""
        return self.stations
    
    def remove_station(self) -> None:
        """Remove a station from the player's count"""
        if self.stations > 0:
            self.stations -= 1
        else:
            raise ValueError("No stations left to remove")
    
    def get_score(self) -> int:
        """Get the player's score"""
        return self.score
    
    def get_claimed_routes(self) -> list:
        """Get the routes claimed by the player"""
        return self.claimed_routes
    
    def add_claimed_route(self, route) -> None:
        """Add a claimed route to the player's list"""
        self.claimed_routes.append(route)

