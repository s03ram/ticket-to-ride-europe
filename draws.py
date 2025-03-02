from random import shuffle

from cards import TrainCard, TicketCard
from data import train_colors, tickets_short, tickets_long


class Trains:
    def __init__(self) -> None:
        self.draw = self.Draw()
        self.discard = self.Discard()
        self.offer = self.Offer(self.draw, self.discard)


    class Draw:
        def __init__(self) -> None:
            self.deck = []
            for color in train_colors:
                for _ in range(12):
                    self.deck.append(TrainCard(color))
            for _ in range(14):
                self.deck.append(TrainCard("locomotive"))
            self.shuffle_it()

        def get_card(self) -> TrainCard:
            return self.deck.pop(0)

        def shuffle_it(self) -> None:
            return shuffle(self.deck)


    class Offer:
        def __init__(self, draw, discard) -> None:
            self.deck = []
            self.check(draw, discard)

        def get_card(self, color) -> TrainCard:
            for train in self.deck:
                if train.get_color() == color:
                    return train
            return "Color not in offer"

        def check(self, draw, discard) -> None:
            self.fill(draw)
            while self.too_much_locomotive():
                for train in self.deck:
                    discard.discard_card(train)
                    self.deck.remove(train)
                self.fill(draw)

        def too_much_locomotive(self) -> bool:
            loco_count = 0
            for card in self.deck:
                if card.color == "locomotive":
                    loco_count += 1
            if loco_count >= 3:
                return True
            return False

        def fill(self, draw):
            while len(self.deck) < 5:
                self.deck.append(draw.get_card())            


    class Discard:
        def __init__(self) -> None:
            self.deck = []

        def discard_card(self, train):
            self.deck.append(train)




class Tickets:
    
    def __init__(self) -> None:
        self.draw = self.Draw()
        self.discard = self.Discard()
    
    
    class Draw:
        def __init__(self) -> None:
            self.short_deck = []
            for ticket in tickets_short:
                self.short_deck.append(TicketCard(ticket["city_a"], ticket["city_b"], ticket["value"]))
                
            self.long_deck = []
            for ticket in tickets_long:
                self.long_deck.append(TicketCard(ticket["city_a"], ticket["city_b"], ticket["value"]))

            shuffle(self.short_deck)
            shuffle(self.long_deck)

        def get_long_ticket(self):
            return self.long_deck.pop(0)

        def get_short_ticket(self):
            return self.short_deck.pop(0)
            
        
    class Discard:
        
        def __init__(self) -> None:
            self.deck = []
            
        def discard_card(self, ticket):
            self.deck.append(ticket)

if __name__ == "__main__":
    trains = Trains()