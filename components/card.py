TRAIN_COLORS = ["grey", "white", "yellow", "red", "orange", "blue", "green", "pink", "locomotive"]


class Card:
    def __init__(self, id: int) -> None:
        """init a card

        Args:
            id (int): the id of the card
        """
        self.id = id

    def get_id(self) -> int:
        return self.id


class TicketCard(Card):
    def __init__(self, id: int, city_a: str, city_b: str, value: int) -> None:
        """init a ticket card

        Args:
            id (int): the id of the ticket card
            city_a (str): starting or arriving city
            city_b (str): starting or arriving city
            value  (int): how many points it gaves
        """
        super().__init__(id)
        self.city_a = city_a
        self.city_b = city_b
        self.value  = value
        
    def get_city_a(self):
        return self.city_a
    
    def get_city_b(self):
        return self.city_b
    
    def get_value(self):
        return self.value


class TrainCard(Card):
    def __init__(self, id: int, color: str) -> None:
        """init a train card

        Args:
            id (int): the id of the train card
            color (str): the color of the train card
        """
        super().__init__(id)
        self.color = color
        
    def get_color(self) -> str:
        return self.color


class City:
    def __init__(self, id: int, name: str) -> None:
        """init a city

        Args:
            id (int): the id of the city
            name (str): the name of the city
        """
        self.id = id
        self.name = name
        
    def get_id(self) -> int:
        return self.id

    def get_name(self) -> str:
        return self.name
