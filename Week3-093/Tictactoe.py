# Tic Tac Toe using Backtracking

board = [' ' for _ in range(9)]


def print_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")
    print()


def is_winner(player):
    win_positions = [
        (0,1,2), (3,4,5), (6,7,8),   # rows
        (0,3,6), (1,4,7), (2,5,8),   # columns
        (0,4,8), (2,4,6)             # diagonals
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False


def is_draw():
    return ' ' not in board


def backtracking_ai():
    # Try to win
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if is_winner('X'):
                return i
            board[i] = ' '

    # Try to block opponent
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if is_winner('O'):
                board[i] = ' '
                return i
            board[i] = ' '

    # Otherwise pick first empty cell
    for i in range(9):
        if board[i] == ' ':
            return i


def play_game():
    print("Tic Tac Toe Game")
    print("You are O | Computer is X")

    while True:
        print_board()

        # Human move
        move = int(input("Enter position (1-9): ")) - 1
        if board[move] != ' ':
            print("Invalid move!")
            continue
        board[move] = 'O'

        if is_winner('O'):
            print_board()
            print("You win!")
            break

        if is_draw():
            print_board()
            print("Draw!")
            break

        # Computer move
        ai_move = backtracking_ai()
        board[ai_move] = 'X'

        if is_winner('X'):
            print_board()
            print("Computer wins!")
            break


play_game()
