print("Tic Tac Toe Game")
board = [[" "," "," "], [" ", " ", " ",], [" ", " ", " "]]

turns = 0
player = "x"
while True:
    print(board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("---------")
    print(board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("---------")
    print(board[2][0] + " | " + board[2][1] + " | " + board[2][2])
    print("Player " + player)
    x = int(input("What is your row?"))
    y = int(input("What is your column"))
    if x > 2:
        print("Invalid move")
        continue
    if y > 2:
        print("Invalid move")
        continue
    if board[x][y] == "x" or board[x][y] == "o":
        print("Invalid move")
        continue
    board[x] [y] = player
    turns = turns + 1
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        print(player + " wins!")
        break
    if board[1][0] == player and board[1][1] == player and board[1][2] == player:
        print(player + " wins!")
        break
    if board[2][0] == player and board[2][1] == player and board[2][2] == player:
        print(player + " wins!")
        break
    if board[0][0] == player and board[1][0] == player and board[2][0] == player:
        print(player + " wins!")
        break
    if board[0][1] == player and board[1][1] == player and board[2][1] == player:
        print(player + " wins!")
        break
    if board[0][2] == player and board[1][2] == player and board[2][2] == player:
        print(player + " wins!")
        break
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        print(player + " wins!")
        break
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        print(player + " wins!")
        break
    if turns == 9:
        print("Tie")
        break

    else:
        if player == "x":
            player = "o"
        else:
            player = "x"