import json
from typing import Dict, List, Optional
from uuid import UUID

import networkx as nx

import data.settings as settings
from src.models.route import Route


class Board:
    def __init__(self) -> None:
        """Represents the board. Initializes the routes and creates the graph."""

        self.routes: Dict[UUID, Route] = {}
        self.__init_routes()
        self.graph = self.__create_weighted_graph()

    def __init_routes(self) -> None:
        """Initialize the routes from the ROUTES data."""
        with open(settings.ROUTES_FILE, "r", encoding="utf-8") as file:
            routes_data = json.load(file)
        for route in routes_data:
            route = Route(**route)
            self.routes[route.id] = route

    def __create_weighted_graph(self) -> nx.MultiGraph:
        """Create a weighted graph from the routes data"""
        board = nx.MultiGraph()
        for id, route in self.routes.items():
            board.add_edge(
                route.city_a,
                route.city_b,
                id=id,
                weight=route.length,
                color=route.color,
                locomotive=route.locomotive,
                tunnel=route.tunnel,
                claimed_by=None,
                stations=[],
            )
        return board

    def get_route(self, route_id: int) -> Optional[Route]:
        """Get a route by ID"""
        return self.routes.get(route_id)

    def get_available_routes(self) -> List[Route]:
        """Get all unclaimed routes"""
        return [route for route in self.routes.values() if not route.is_claimed()]

    def get_routes_between_cities(self, city1: str, city2: str) -> List[Route]:
        """Get all routes between two cities"""
        return [
            route
            for route in self.routes.values()
            if {route.city_a, route.city_b} == {city1, city2}
        ]

    def claim_route(self, route_id: str, player_id: UUID) -> bool:
        """Claim a route for a player"""
        route = self.get_route(route_id)
        if route and not route.is_claimed():
            route.claimed_by = player_id
            return True
        return False
