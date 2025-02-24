import os

from random import shuffle
from boards import Board
from players import Player
from data import players_colors, MEDIAS_REPERTORY, train_colors


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


def display_items(items):
    [print(item) for item in items]
    

def display_hand(player):
    print("   TRAINS DECK :")
    display_items(player.train_cards_deck)
    print("\n   TICKETS DECK :")
    display_items(player.tickets_deck)
    print("\n   TRAINS")
    print(player.trains)
    print("\n   STATIONS")
    print(player.stations)
    input("\nPress ENTER")



def draw_train():
    items = board.trains_draw.offer.deck
    items.append("random")
    display_items(items)


def main_menu():
    clear()
    items = [
        "MAIN MENU",
        "1 - Display hand",
        "2 - Draw train",
        "3 - Draw ticket",
        "4 - Claim route",
        "5 - Build station",
        "6 - Exit"
    ]
    display_items(items)
    
    choice = input("\n>>> ")
    if choice == "1":
        clear()
        display_hand(player)

    elif choice == "2":
        clear()
        draw_train()
        input()
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        exit()



# Setting up the game
board = Board()
# Setting up players
players = init_players(2, board.trains_draw.draw, board.tickets_draw.draw)

#############
# Game loop #
clear()
playing = True
while playing:
    for player in players:
        main_menu()
