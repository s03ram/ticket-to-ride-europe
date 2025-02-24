import networkx as nx
import matplotlib.pyplot as plt

from data import routes
from draws import Trains, Tickets
from players import Player


class Board:

    def __init__(self) -> None:
        """Represents the board
        
        Variables :
            - trains    (Trains object): trains cards draw/discard/offer
            - tickets  (Tickets object): destination tickets cards draw/discard
            - board (Multigraph object): graph that represents the game board
        
        Methods :
            - show() : show the borad as a graph
            
        """
        self.trains_draw = Trains()
        self.tickets_draw = Tickets()
        
        # Create a weighted graph (the board)
        self.board = nx.MultiGraph()
        for route in routes:
            self.board.add_edge(
                route["city_a"],
                route["city_b"],
                weight     = route["lenght"],
                color      = route["color"],
                locomotive = route["locomotive"],
                tunnel     = route["tunnel"],
                owner = "",
                stations = [])

            
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


if __name__ == "__main__":
    board = Board()
    board.show()
