import json
import random
from typing import Dict, List, Optional
from uuid import UUID, uuid4

from src.board import Board
from src.models.cards import DestinationTicket
from src.models.city import City
from src.models.deck import DestinationTicketDeck, TrainCardDeck
from src.models.game import GamePhase, GameState
from src.models.player import Player


class GameInitializer:
    """Handles initialization of a new Ticket to Ride game"""

    # Standard game configuration
    INITIAL_TRAINS = 45
    INITIAL_TRAIN_CARDS = 4
    INITIAL_DESTINATION_TICKETS_DRAWN = 3
    MIN_INITIAL_DESTINATION_TICKETS = 2

    PLAYER_COLORS = ["red", "blue", "green", "yellow", "black"]

    def __init__(
        self,
        destination_tickets_file: Optional[str] = None,
    ):
        """
        Initialize the game initializer

        Args:
            destination_tickets_file: Path to JSON file with destination tickets
        """
        self.destination_tickets_file = destination_tickets_file

    def load_destination_tickets(self) -> List[DestinationTicket]:
        """
        Load destination tickets from JSON file

        Expected JSON format:
        [
            {
                "city_a": "Los Angeles",
                "city_b": "New York",
                "points": 21
            },
            ...
        ]
        """
        if not self.destination_tickets_file:
            raise ValueError("Destination tickets file path not provided")

        tickets = []
        with open(self.destination_tickets_file, "r", encoding="utf-8") as file:
            tickets_data = json.load(file)

        for ticket_data in tickets_data:
            ticket = DestinationTicket(
                city_a=City(name=ticket_data["city_a"]),
                city_b=City(name=ticket_data["city_b"]),
                points=ticket_data["points"],
                length="short" if ticket_data["points"] < 20 else "long",
            )
            tickets.append(ticket)

        return tickets

    def create_players(self, player_names: List[str], player_ids: Optional[List[UUID]] = None) -> List[Player]:
        """
        Create player objects for the game

        Args:
            player_names: List of player names
            player_ids: Optional list of player UUIDs (for reconnection)

        Returns:
            List of Player objects
        """
        if len(player_names) < 2 or len(player_names) > 5:
            raise ValueError("Game requires 2-5 players")

        if player_ids and len(player_ids) != len(player_names):
            raise ValueError("Number of player IDs must match number of names")

        players = []
        for i, name in enumerate(player_names):
            player = Player(
                id=player_ids[i] if player_ids else uuid4(),
                name=name,
                trains_remaining=self.INITIAL_TRAINS,
                score=0,
                color=self.PLAYER_COLORS[i],
                train_cards=[],
                destination_tickets=[],
            )
            players.append(player)

        return players

    def setup_train_deck(self, train_deck: TrainCardDeck) -> None:
        """
        Initialize and shuffle the train card deck
        Sets up the draw pile and 5 face-up cards
        """
        train_deck.initialize_deck()

        # If 3+ locomotives are face-up initially, refresh
        while train_deck.check_too_many_locomotives():
            train_deck.refresh_face_up_cards()

    def setup_destination_deck(self, destination_deck: DestinationTicketDeck) -> None:
        """
        Load and shuffle destination tickets
        """
        tickets = self.load_destination_tickets()
        destination_deck.initialize_deck(tickets)

    def deal_initial_cards(self, players: List[Player], train_deck: TrainCardDeck) -> None:
        """
        Deal initial train cards to all players
        Each player gets 4 train cards
        """
        for player in players:
            for _ in range(self.INITIAL_TRAIN_CARDS):
                card = train_deck.draw_card()
                if card:
                    player.train_cards.append(card)

    def deal_initial_destination_tickets(
        self, players: List[Player], destination_deck: DestinationTicketDeck
    ) -> Dict[UUID, List[DestinationTicket]]:
        """
        Deal initial destination tickets to all players
        Each player draws 3 tickets and must keep at least 2

        Returns:
            Dict mapping player_id to their drawn tickets (for selection)
        """
        drawn_tickets = {}

        for player in players:
            tickets = destination_deck.draw_tickets(self.INITIAL_DESTINATION_TICKETS_DRAWN)
            drawn_tickets[player.id] = tickets

        return drawn_tickets

    def finalize_initial_tickets(
        self,
        player: Player,
        tickets_to_keep: List[DestinationTicket],
        tickets_to_discard: List[DestinationTicket],
        destination_deck: DestinationTicketDeck,
    ) -> bool:
        """
        Finalize a player's initial destination ticket selection

        Args:
            player: The player selecting tickets
            tickets_to_keep: Tickets the player wants to keep
            tickets_to_discard: Tickets to return to the deck
            destination_deck: The destination ticket deck

        Returns:
            True if selection is valid, False otherwise
        """
        if len(tickets_to_keep) < self.MIN_INITIAL_DESTINATION_TICKETS:
            return False

        # Add kept tickets to player's hand
        player.destination_tickets.extend(tickets_to_keep)

        # Return discarded tickets to the deck
        destination_deck.discard_pile.extend(tickets_to_discard)

        return True

    def determine_first_player(self, players: List[Player]) -> int:
        """
        Randomly determine which player goes first

        Returns:
            Index of the starting player
        """
        return random.randint(0, len(players) - 1)

    def initialize_game(
        self, player_names: List[str], player_ids: Optional[List[UUID]] = None
    ) -> tuple[GameState, Dict[UUID, List[DestinationTicket]]]:
        """
        Complete game initialization process

        Args:
            player_names: List of player names
            player_ids: Optional list of player UUIDs

        Returns:
            Tuple of (GameState, pending_destination_tickets)
            The GameState is ready to play after players select their initial tickets
        """
        # Create board (uses your existing Board class)
        board = Board()

        # Create players
        players = self.create_players(player_names, player_ids)

        # Create game state
        game_state = GameState(players=players, board=board)

        # Setup train card deck
        self.setup_train_deck(game_state.train_deck)

        # Setup destination ticket deck
        self.setup_destination_deck(game_state.destination_deck)

        # Deal initial train cards
        self.deal_initial_cards(players, game_state.train_deck)

        # Deal initial destination tickets (players need to select)
        pending_tickets = self.deal_initial_destination_tickets(players, game_state.destination_deck)

        # Determine starting player
        starting_player_index = self.determine_first_player(players)
        game_state.current_player_index = starting_player_index

        # Game starts in SETUP phase until all players select their tickets
        game_state.phase = GamePhase.SETUP

        return game_state, pending_tickets


class GameInitializationManager:
    """
    Manages the game initialization flow including player ticket selection
    """

    def __init__(self, game_state: GameState):
        self.game_state = game_state
        self.pending_ticket_selections: Dict[UUID, List[DestinationTicket]] = {}
        self.players_ready: set[UUID] = set()

    def set_pending_tickets(self, pending_tickets: Dict[UUID, List[DestinationTicket]]) -> None:
        """Set the initial destination tickets that players need to select"""
        self.pending_ticket_selections = pending_tickets

    def player_select_initial_tickets(self, player_id: UUID, ticket_ids_to_keep: List[UUID]) -> tuple[bool, str]:
        """
        Handle a player's initial destination ticket selection

        Args:
            player_id: ID of the player
            ticket_ids_to_keep: List of ticket IDs the player wants to keep

        Returns:
            (success, message) tuple
        """
        if player_id not in self.pending_ticket_selections:
            return False, "No pending ticket selection for this player"

        if player_id in self.players_ready:
            return False, "Player has already selected tickets"

        drawn_tickets = self.pending_ticket_selections[player_id]

        if len(ticket_ids_to_keep) < GameInitializer.MIN_INITIAL_DESTINATION_TICKETS:
            return False, f"Must keep at least {GameInitializer.MIN_INITIAL_DESTINATION_TICKETS} tickets"

        if len(ticket_ids_to_keep) > len(drawn_tickets):
            return False, "Cannot keep more tickets than drawn"

        # Map ticket IDs to actual tickets
        # ticket_map = {ticket.id: ticket for ticket in drawn_tickets}
        tickets_to_keep = []
        tickets_to_discard = []

        for ticket in drawn_tickets:
            if ticket.id in ticket_ids_to_keep:
                tickets_to_keep.append(ticket)
            else:
                tickets_to_discard.append(ticket)

        # Validate all IDs are valid
        if len(tickets_to_keep) != len(ticket_ids_to_keep):
            return False, "Invalid ticket IDs provided"

        # Add tickets to player's hand
        player = self.game_state.get_player(player_id)
        initializer = GameInitializer()

        success = initializer.finalize_initial_tickets(
            player, tickets_to_keep, tickets_to_discard, self.game_state.destination_deck
        )

        if not success:
            return False, "Failed to finalize ticket selection"

        # Mark player as ready
        self.players_ready.add(player_id)

        # Check if all players are ready
        if len(self.players_ready) == len(self.game_state.players):
            self.game_state.phase = GamePhase.PLAYING
            return True, f"Selected {len(tickets_to_keep)} tickets. Game is starting!"

        return True, f"Selected {len(tickets_to_keep)} tickets. Waiting for other players..."

    def all_players_ready(self) -> bool:
        """Check if all players have selected their initial tickets"""
        return len(self.players_ready) == len(self.game_state.players)

    def get_pending_players(self) -> List[UUID]:
        """Get list of player IDs that haven't selected tickets yet"""
        return [player_id for player_id in self.pending_ticket_selections.keys() if player_id not in self.players_ready]


if __name__ == "__main__":
    # Example usage
    initializer = GameInitializer(destination_tickets_file="data/tickets.json")

    player_names = ["Alice", "Bob", "Charlie"]
    game_state, pending_tickets = initializer.initialize_game(player_names)

    manager = GameInitializationManager(game_state)
    manager.set_pending_tickets(pending_tickets)

    # Simulate players selecting tickets
    for player in game_state.players:
        drawn_tickets = pending_tickets[player.id]
        ticket_ids_to_keep = [ticket.id for ticket in drawn_tickets[:2]]  # Keep first 2 tickets
        success, message = manager.player_select_initial_tickets(player.id, ticket_ids_to_keep)
        print(f"Player {player.name}: {message}")

    if game_state.phase == GamePhase.PLAYING:
        print("Game is now in PLAYING phase!")
