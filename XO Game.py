import random

# Create a 3x3 board
board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

# Print the board function
def print_board(board):
    for row in board:
        print(' '.join(row))

# Check if the game is over function
def game_over(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '-':
            return True
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '-':
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return True
    return False

# Main game loop
while not game_over(board):
    # Player X's turn
    print_board(board)
    while True:
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        if board[row][col] == '-':
            board[row][col] = 'X'
            break
        else:
            print("That spot is already taken, try again.")
    if game_over(board):
        break

    # Computer O's turn
    print_board(board)
    print("Computer O's turn")
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == '-':
            board[row][col] = 'O'
            break
    if game_over(board):
        break

# Game over
print_board(board)
if game_over(board):
    if 'X' in board[0]:
        print('Player X wins!')
    elif 'X' in board[1]:
        print('Player X wins!')
    elif 'X' in board[2]:
        print('Player X wins!')
    elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        print('Player X wins!')
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        print('Player X wins!')
    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        print('Player X wins!')
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        print('Player X wins!')
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        print('Player X wins!')
    else:
        print('Computer O wins!')
else:
    print('Tie game!')
