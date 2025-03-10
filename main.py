from components.game import GameController
from components.players import Player


def main():
    # Add players
    player1 = Player("red")
    player2 = Player("black")

    # Initialize game
    controller = GameController([player1, player2])

    # TODO why do ot work?
    print(player1)

    while True:
        current_player = controller.players[controller.current_player_index]
        # Show face-up cards
        print("\nFace up cards:")
        for i, card in enumerate(controller.game.face_up_cards):
            print(f"{i}: {card}")

        # Prompt player for action
        print("\nChoose an action:")
        print("1: Draw face-up card")
        print("2: Draw from deck")
        action = input("Enter the number of your action: ")

        if action == "1":
            card_index = int(input("Which card would you like to draw? : "))
            turn_complete = controller.handle_card_draw(
                current_player,
                card_index=card_index
                )
        elif action == "2":
            turn_complete = controller.handle_card_draw(
                current_player
                )
        else:
            print("Invalid action. Please try again.")
            continue

        if turn_complete:
            break

    # Show player's cards
    print(f"\n{current_player.color}'s cards:")
    for card in current_player.train_cards:
        print(card)


if __name__ == "__main__":
    main()
