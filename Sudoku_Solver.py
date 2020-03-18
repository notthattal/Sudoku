from sudoku_setup import *

#This is a sudoku solver AI
def sudoku_solver(board):
    global ELEMENTS
    zero = next_zero(board)
    if len(zero) == 0:
        return 1
    else:
        i = zero[0]
        j = zero[1]
    for k in ELEMENTS:
        valid = valid_move(board,i,j,k)
        if valid == 1:
            add_move(board,i,j,k)
            if sudoku_solver(board):
                return 1
            board[i,j] = 0
    return 0