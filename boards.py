from data import routes, cities


class Board:
    def __init__(self) -> None:
        """Represent the board
        Attributes :
            - routes (dict): dictionnary of routes
            - cities (list): list of cities
        """
        self.routes = routes
        self.cities = cities
