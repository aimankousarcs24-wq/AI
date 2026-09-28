board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]


def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_win(player):
    wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for a, b, c in wins:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False


def full():
    for x in board:
        if x != "X" and x != "O":
            return False
    return True


def minimax(computer_turn):
    if check_win("O"):
        return 1

    if check_win("X"):
        return -1

    if full():
        return 0

    if computer_turn:
        best = -2

        for i in range(9):
            if board[i] != "X" and board[i] != "O":

                old = board[i]
                board[i] = "O"

                score = minimax(False)

                board[i] = old

                if score > best:
                    best = score

        return best

    else:
        best = 2

        for i in range(9):
            if board[i] != "X" and board[i] != "O":

                old = board[i]
                board[i] = "X"

                score = minimax(True)

                board[i] = old

                if score < best:
                    best = score

        return best


def computer_move():
    best_score = -2
    best_position = -1

    for i in range(9):

        if board[i] != "X" and board[i] != "O":

            old = board[i]
            board[i] = "O"

            score = minimax(False)

            board[i] = old

            if score > best_score:
                best_score = score
                best_position = i

    board[best_position] = "O"


print("TIC TAC TOE")
print("You = X")
print("Computer = O")

while True:

    display_board()

    # Human turn
    while True:

        try:
            position = int(input("Enter position (1-9): "))

            if position < 1 or position > 9:
                print("Invalid position. Enter 1 to 9.")
                continue

            position = position - 1

            if board[position] == "X" or board[position] == "O":
                print("Position already occupied.")
                continue

            board[position] = "X"
            break

        except ValueError:
            print("Enter a number from 1 to 9.")

    display_board()

    if check_win("X"):
        print("You win!")
        break

    if full():
        print("Draw!")
        break

    # Computer turn
    print("Computer's turn...")
    computer_move()

    if check_win("O"):
        display_board()
        print("Computer wins!")
        break

    if full():
        display_board()
        print("Draw!")
        break
