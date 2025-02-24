class TrainCard:
    def __init__(self, color: str) -> None:
        """init a train card

        Args:
            color (str): the color of the train card
        """
        self.color = color
        
    def __repr__(self):
        return self.color
        
    def get_color(self) -> str:
        return self.color
    

class TicketCard:
    def __init__(self, city_a: str, city_b: str, value: int) -> None:
        """init a short destination ticket

        Args:
            city_a (str): starting or arriving city
            city_b (str): starting or arriving city
            value  (int): how many points it gaves
        """
        self.city_a = city_a
        self.city_b = city_b
        self.value  = value
    
    def __repr__(self):
        return f"{self.city_a} -> {self.city_b} : {self.value}"
    
    def get_city_a(self):
        return self.city_a
    
    def get_city_b(self):
        return self.city_b
    
    def get_value(self):
        return self.value


