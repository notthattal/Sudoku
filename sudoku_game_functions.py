
import numpy as np

#Define Global Variables
ROWS = 9
COLUMNS = 9
ELEMENTS = [1,2,3,4,5,6,7,8,9]

#Function to check if a move is valid
#Inputs:
#   board - the current state of the game board
#   row - the desired row you would like to put a number
#   col - the desired column you would like to put a number
#   num - the desired number you would like to enter
def valid_move(board, row, col, num):
    if num in board[row] or num in board[:, col]:
        return 0
    elif row <= 2 and col <= 2 and num in board[0:3, 0:3]:
        return 0
    elif row <= 2 and col > 2 and col <= 5 and num in board[0:3, 3:6]:
        return 0
    elif row <= 2 and col > 5 and col <= 8 and num in board[0:3, 6:9]:
        return 0
    elif row > 2 and row <= 5 and col <= 2 and num in board[3:6, 0:3]:
        return 0
    elif row > 5 and row <= 8 and col <= 2 and num in board[6:9, 0:3]:
        return 0
    elif row > 2 and row <= 5 and col > 2 and col <= 5 and num in board[3:6, 3:6]:
        return 0
    elif row > 5 and row <= 8 and col > 2 and col <= 5 and num in board[6:9, 3:6]:
        return 0
    elif row > 2 and row <= 5 and col > 5 and col <= 8 and num in board[3:6, 6:9]:
        return 0
    elif row > 5 and row <= 8 and col > 5 and col <= 8 and num in board[6:9, 6:9]:
        return 0
    else:
        return 1

#If a move is valid this function adds the move to the board
#and returns 1, otherwise it returns 0
#Inputs:
#   board - the current state of the game board
#   row - the desired row you would like to put a number
#   col - the desired column you would like to put a number
#   num - the desired number you would like to enter
def add_move(board,row,col,num):
    valid = valid_move(board,row,col,num)
    if(valid == 1):
        board[row,col] = num
        return 1
    else:
        return 0

#Checks the next empty space in the board
#returns the row and column if there is an empty space in the board
#otherwise this returns an empty array
#Inputs:
#   board - the current state of the game board
def next_zero(board):
    for i in range(ROWS):
        for j in range(COLUMNS):
            if board[i,j] == 0:
                return [i,j]

    return []

#This function let's the player add moves
#The input is the current state of the board
def player_move(board):
    move = 0
    if 0 not in board:
        print("There are no valid moves")
        return 0

    while move == 0:
        print("enter the row, column and number you would like to put a number in \neach should be a number between 1 and 9: ")
        row = input("row: ")
        row = int(row)
        col = input("column: ")
        col = int(col)
        num = input("number: ")
        num = int(num)
        row = row-1
        col = col-1
        move = add_move(board,row,col,num)
        if move == 1:
            return 1
        else:
            print("Those aren't valid inputs")

#This function checks if a completed board's
#solution was a valid solution
def check_win(board):
    if 0 in board:
        return 0
    else:
        for i in range(1,10):
            for j in range(ROWS):
                for k in range(COLUMNS):
                    if np.count_nonzero(board[j] == i) > 1 or np.count_nonzero(board[:, k] == i) >1:
                        return 0
                    elif j <= 2 and k <= 2 and np.count_nonzero(board[0:3, 0:3] == i) > 1:
                        return 0
                    elif j <= 2 and k > 2 and k <= 5 and np.count_nonzero(board[0:3, 3:6] == i) > 1:
                        return 0
                    elif j <= 2 and k > 5 and k <= 8 and np.count_nonzero(board[0:3, 6:9] == i) > 1:
                        return 0
                    elif j > 2 and j <= 5 and k <= 2 and np.count_nonzero(board[3:6, 0:3] == i) > 1:
                        return 0
                    elif j > 5 and j <= 8 and k <= 8 and np.count_nonzero(board[6:9, 0:3] == i) > 1:
                        return 0
                    elif j > 2 and j <= 5 and k > 2 and np.count_nonzero(board[3:6, 3:6] == i) > 1:
                        return 0
                    elif j > 5 and j <= 8 and k > 2 and k <= 5 and np.count_nonzero(board[6:9, 3:6] == i) > 1:
                        return 0
                    elif j > 2 and j <= 5 and k > 5 and k <= 8 and np.count_nonzero(board[3:6, 6:9] == i) > 1:
                        return 0
                    elif j > 5 and j <= 8 and k > 5 and k <= 8 and np.count_nonzero(board[6:9, 6:9] == i) > 1:
                        return 0

        return 1
