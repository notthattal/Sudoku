from sudoku_game_functions import *
import random

#function which displays the sudoku board
#board is the current state of the game board
def display_sudoku_board(board):
    for i in range(ROWS):
        if i == 3 or i == 6:
            print("- - - - - - - - - - - - - ")
        for j in range(COLUMNS):
            if j == 3 or j == 6:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

#Helper function to create a board
def sudoku_pattern(r, c, block):
    return (block * (r % block) + r // block + c) % (block*block)

#helper function to create a board
def shuffle(s):
    return random.sample(s, len(s))

#function to create a random sudoku board
def make_sudoku_board():
    block = 3
    side = 9
    row_base = range(block)
    row = [i * block + r for i in shuffle(row_base) for r in shuffle(row_base)]
    col = [i * block + c for i in shuffle(row_base) for c in shuffle(row_base)]
    nums = shuffle(range(1, side + 1))
    board = np.array([[nums[sudoku_pattern(r, c, block)] for c in col] for r in row])
    win = check_win(board)
    if win is 1:
        i = 0
        while i <= 50:
            row = random.randint(0,8)
            col = random.randint(0,8)
            board[row,col] = 0
            i += 1
    return board