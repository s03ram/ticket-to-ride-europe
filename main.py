from game import GameController
from players import Player


def main():
    # Initialize game
    controller = GameController()

    # Add players
    player1 = Player("red")
    player2 = Player("black")
    controller.players = [player1, player2]

    # Example turn
    current_player = player1

    # Show face-up cards
    print("Face up cards:")
    for i, card in enumerate(controller.game.face_up_cards):
        print(f"{i}: {card}")

    # First draw - face up card
    turn_complete = controller.handle_card_draw(current_player, card_index=0)
    if not turn_complete:
        # Second draw - from deck
        turn_complete = controller.handle_card_draw(current_player)

    # Show player's cards
    print(f"\n{current_player.color}'s cards:")
    for card in current_player.train_cards:
        print(card)


if __name__ == "__main__":
    main()
