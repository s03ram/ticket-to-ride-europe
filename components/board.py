import networkx as nx
import matplotlib.pyplot as plt

from data import ROUTES, TICKETS_SHORT, TICKETS_LONG
from .card import TicketCard, TrainCard, TRAIN_COLORS
from .deck import Deck
from .utils import generate_id_list


class Board:
    def __init__(self) -> None:
        """Represents the board
        """
        self.trains_draw = Deck()
        self.trains_offer = Deck()
        self.long_tickets_draw = Deck()
        self.short_tickets_draw = Deck()
        self.board = self.create_weighted_graph()
        
        self.init_trains_draws()
        self.init_tickets_draws()


    def init_trains_draws(self) -> None:
        """Initialize the trains draw deck
        """
        ids = generate_id_list(110, (1000,2000))
        for color in TRAIN_COLORS:
            for _ in range(12):
                self.trains_draw.add_card(TrainCard(color=color, id=ids.pop(0)))
        for _ in range(2):
            self.trains_draw.add_card(TrainCard(color="locomotive", id=ids.pop(0)))
        self.trains_draw.shuffle()


    def init_tickets_draws(self) -> None:
        """Initialize the tickets draw deck
        """
        ids = generate_id_list(len(TICKETS_SHORT) + len(TICKETS_LONG), (2000, 3000))
        for ticket in TICKETS_SHORT:
            self.short_tickets_draw.add_card(TicketCard(
                id=ids.pop(0),
                city_a=ticket["city_a"],
                city_b=ticket["city_b"],
                value=ticket["value"]
                ))
        for ticket in TICKETS_LONG:
            self.long_tickets_draw.add_card(TicketCard(
                id=ids.pop(0),
                city_a=ticket["city_a"],
                city_b=ticket["city_b"],
                value=ticket["value"]
                ))
        self.short_tickets_draw.shuffle()
        self.long_tickets_draw.shuffle()


    def create_weighted_graph(self) -> nx.MultiGraph:
        """Create a weighted graph from the routes data
        """
        board = nx.MultiGraph()
        for route in ROUTES:
            board.add_edge(
                route["city_a"],
                route["city_b"],
                weight     = route["lenght"],
                color      = route["color"],
                locomotive = route["locomotive"],
                tunnel     = route["tunnel"],
                owner      = None,
                stations   = [])
        return board


    def get_trains_draw(self) -> Deck:
        """Get the trains draw deck
        """
        return self.trains_draw


    def get_trains_offer(self) -> Deck:
        """Get the trains draw deck
        """
        return self.trains_offer


    def get_tickets_draw(self, ticket_type: str) -> Deck:
        """Get the "long" or "short" tickets draw deck
        """
        if ticket_type == "short":
            return self.short_tickets_draw
        elif ticket_type == "long": 
            return self.long_tickets_draw
        else:
            raise ValueError("Invalid ticket type. Use 'short' or 'long'.")


    def show(self):
        """Show the board under the graph form
        """
        # Draw the graph
        pos = nx.spring_layout(self.board)  # positions for all nodes
        nx.draw(self.board, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=16, font_color='black')
        edge_labels = nx.get_edge_attributes(self.board, 'weight')
        nx.draw_networkx_edge_labels(self.board, pos, edge_labels=edge_labels)

        # Display the plot
        plt.title("Ticket to Ride : Europe")
        plt.show()
