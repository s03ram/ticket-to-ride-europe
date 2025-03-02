import os

from random import shuffle
from boards import Board
from players import Player
from data import players_colors, train_colors


def init_players(players_amount:int, trains_draw, tickets_draw):
    """initialize a list of players classes
    Min 2 and Max 5

    Args:
        players_amount (int): number of players
    """
    assert 2 <= players_amount <= 5, "Between 2 and 5 players required"
    
    shuffle(players_colors)
    players = []
    for i in range(players_amount):
        players.append(Player(players_colors[i], trains_draw, tickets_draw))
    return players


def count_train_cards_color(player) -> dict:
    """Returns a dictionnary with as key the color of the card
    and as value the amount of cards of this color
    """
    result = {}
    for color in train_colors:
        result[color] = 0
    for card in player.train_cards_deck:
        result[card.color] += 1
    return result


def check_trains_draw_offer():
    board.trains_draw.offer.check(board.trains_draw.draw, board.trains_draw.discard)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_items(items, exept_first=False):
    
    if exept_first:
        print(items[0])
        for i in range(1, len(items)):
            print(f"{i} - {items[i]}")
    else:
        for i in range(len(items)):
            print(f"{i+1} - {items[i]}")


def display_hand(player):
    print(player)
    input("\nPress ENTER")


def draw_train():
    items = board.trains_draw.offer.deck
    if "random" not in items:
        items.append("random")
    display_items(items)

    choice = input("\n>>> ")
    if choice == "random":
        board.trains_draw.draw.get_card()
    else:
        train = board.trains_draw.offer.get_card(int(choice))
        print(f"You get : {train}")
        input("\nPress ENTER")


def main_menu(player):
    clear()
    print(player,"\n")
    items = [
        "MAIN MENU",
        "Draw train",
        "Draw ticket",
        "Claim route",
        "Build station",
        "Exit"
    ]
    display_items(items, True)
    
    choice = input("\n>>> ")
    if choice == "1":
        clear()
        print(player,"\n")
        draw_train()
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        exit()



# Setting up the game
board = Board()
# Setting up players
players = init_players(2, board.trains_draw.draw, board.tickets_draw.draw)

#############
# Game loop #
try:
    clear()
    playing = True
    while playing:
        for player in players:
            main_menu(player)
except KeyboardInterrupt:
    print("\n\nGame interrupted")
    exit()
except Exception as e:
    print("\n\nError :", e)
    exit()

