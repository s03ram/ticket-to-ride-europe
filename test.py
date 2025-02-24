from boards import Board

fail = 0

for i in range(10_000):
    board = Board()
    board.trains_draw.offer.check(board.trains_draw.draw, board.trains_draw.discard)
    
    loco_count = 0
    for card in board.trains_draw.offer.deck :
        if card.color == "locomotive":
            loco_count += 1
    if loco_count >= 3:
        fail +=1

print(fail)

