import copy

# these codes indicate the status of a position in the board
CONST_CODE_EMPTY = 0
CONST_CODE_BLOCKED = -1
CONST_CODE_QUEEN = 1

def print_board(board):
    for row in starting_board:
        for col in row:
            if (col == CONST_CODE_QUEEN):
                print ('Q', end=" ")
            else:
                print('_', end=" ")
        print()

# insert a queen (1) into a board at a given location, from 1 to 8 inclusively
def insert_queen(board, row, col):
    # if location outside of board, return false
    if (row < 1 > col or row > 8 < col):
        return False
    # if queen cannot be placed in given location, return false
    if (board[row][col] == CONST_CODE_BLOCKED or board[row][col] == CONST_CODE_QUEEN):
        return False
    board[row][col] = CONST_CODE_QUEEN

    return True

size = 8
starting_board = [[0 for x in range(size)] for y in range(size)]
print_board(starting_board)
print(insert_queen(starting_board, 1, 1))