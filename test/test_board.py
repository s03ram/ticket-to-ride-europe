import networkx as nx

from unittest import TestCase
from uuid import uuid4

from src.board import Board


class TestBoard(TestCase):
    def setUp(self):
        self.board = Board()

    def test_initialization(self):
        self.assertIsInstance(self.board.graph, nx.MultiGraph)
        self.assertGreater(len(self.board.routes), 0)

    def test_get_route(self):
        some_route_id = next(iter(self.board.routes))
        route = self.board.get_route(some_route_id)
        self.assertIsNotNone(route)
        self.assertEqual(route.id, some_route_id)

    def test_get_available_routes(self):
        available_routes = self.board.get_available_routes()
        for route in available_routes:
            self.assertFalse(route.is_claimed())

    def test_get_routes_between_cities(self):
        some_route = next(iter(self.board.routes.values()))
        routes_between = self.board.get_routes_between_cities(
            some_route.city_a.name, some_route.city_b.name
        )
        self.assertIn(some_route, routes_between)

    def test_claim_route(self):
        some_route_id = next(iter(self.board.routes))
        player_id = uuid4()
        success = self.board.claim_route(some_route_id, player_id)
        self.assertTrue(success)
        route = self.board.get_route(some_route_id)
        self.assertTrue(route.is_claimed())

    def test_claim_station(self):
        some_city = next(iter(self.board.cities.values()))
        player_id = uuid4()
        success = self.board.claim_station(some_city.id, player_id)
        self.assertTrue(success)
        self.assertTrue(some_city.station_is_claimed())
        self.assertEqual(some_city.station_claimed_by, player_id)
