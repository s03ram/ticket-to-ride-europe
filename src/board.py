import networkx as nx
import json

import data.settings as settings
from data.models.route import Route
from typing import Optional, List
from uuid import UUID


class Board:
    def __init__(self) -> None:
        """Represents the board. Initializes the routes and creates the graph."""

        self.board = self.__create_weighted_graph()
        self.routes: list[Route] = []
        self.__init_routes()

    def __init_routes(self) -> None:
        """Initialize the routes from the ROUTES data."""
        with open(settings.ROUTES_FILE, "r", encoding="utf-8") as file:
            routes_data = json.load(file)
        [self.routes.append(Route(**route)) for route in routes_data]

    def __create_weighted_graph(self) -> nx.MultiGraph:
        """Create a weighted graph from the routes data
        """
        board = nx.MultiGraph()
        for route in self.routes:
            board.add_edge(
                route.city_a,
                route.city_b,
                id         = route.id,
                weight     = route.length,
                color      = route.color,
                locomotive = route.locomotive,
                tunnel     = route.tunnel,
                claimed_by = None,
                stations   = [])
        return board

    def get_route(self, route_id: str) -> Optional[Route]:
        """Get a route by ID"""
        return self.routes.get(route_id)
    
    def get_available_routes(self) -> List[Route]:
        """Get all unclaimed routes"""
        return [route for route in self.routes.values() if not route.is_claimed()]
    
    def get_routes_between_cities(self, city1: str, city2: str) -> List[Route]:
        """Get all routes between two cities"""
        return [
            route for route in self.routes.values()
            if {route.city1, route.city2} == {city1, city2}
        ]
    
    def claim_route(self, route_id: str, player_id: UUID) -> bool:
        """Claim a route for a player"""
        route = self.get_route(route_id)
        if route and not route.is_claimed():
            route.claimed_by = player_id
            return True
        return False
