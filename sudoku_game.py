from Sudoku_Solver import *
from datetime import datetime

def main():
    random.seed(datetime.now())
    board = make_sudoku_board()
    display_sudoku_board(board)
    sudoku_solver(board)
    print('\n')
    if check_win(board) == 1:
        display_sudoku_board(board)


main()