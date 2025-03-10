import unittest
from components.game import Game, DrawError, DrawPhase
from components.cards import TrainCard, TrainColor
from components.decks import TrainDeck


class MockTrainDeck(TrainDeck):
    def __init__(self, cards):
        self.cards = cards
        self.discard_pile = []

    def draw(self):
        return self.cards.pop(0)

    def discard(self, card):
        self.discard_pile.append(card)


class TestGame(unittest.TestCase):
    def setUp(self):
        self.mock_deck = MockTrainDeck([
            TrainCard(TrainColor.RED), TrainCard(TrainColor.BLUE),
            TrainCard(TrainColor.LOCOMOTIVE), TrainCard(TrainColor.GREEN),
            TrainCard(TrainColor.YELLOW), TrainCard(TrainColor.LOCOMOTIVE),
            TrainCard(TrainColor.LOCOMOTIVE), TrainCard(TrainColor.LOCOMOTIVE)
        ])
        self.game = Game()
        self.game.train_deck = self.mock_deck
        self.game.face_up_cards = [self.mock_deck.draw() for _ in range(5)]
        self.game._check_face_up_cards()

    def test_initial_face_up_cards(self):
        self.assertEqual(len(self.game.face_up_cards), 5)

    def test_draw_face_up_card(self):
        card = self.game.draw_face_up_card(0)
        self.assertEqual(card.color, TrainColor.RED)
        self.assertEqual(len(self.game.face_up_cards), 5)

    def test_draw_invalid_card_index(self):
        with self.assertRaises(DrawError):
            self.game.draw_face_up_card(5)

    def test_draw_locomotive_as_second_card(self):
        self.game.draw_phase = DrawPhase.FIRST_CARD
        with self.assertRaises(DrawError):
            self.game.draw_face_up_card(2)

    def test_check_face_up_cards(self):
        self.game.face_up_cards = [
            TrainCard(TrainColor.LOCOMOTIVE),
            TrainCard(TrainColor.LOCOMOTIVE),
            TrainCard(TrainColor.LOCOMOTIVE),
            TrainCard(TrainColor.RED),
            TrainCard(TrainColor.BLUE)
        ]
        self.game._check_face_up_cards()
        self.assertEqual(len(self.game.face_up_cards), 5)
        self.assertLessEqual(
            sum(
                1 for card in self.game.face_up_cards
                if card.color == TrainColor.LOCOMOTIVE
                ), 2
        )

    def test_draw_from_deck(self):
        card = self.game.draw_from_deck()
        self.assertEqual(card.color, TrainColor.GREEN)


if __name__ == '__main__':
    unittest.main()
