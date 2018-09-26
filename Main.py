import copy

# these codes indicate the status of a position in the board
CONST_CODE_EMPTY = 0
CONST_CODE_BLOCKED = -1
CONST_CODE_QUEEN = 1
class Board:
    def __init__(self, size):
        self._size=size
        self._queen_count = 0
        self._board=[[0 for x in range(size)] for y in range(size)]
        return

    def get_size(self):
        return self._size

    def get_queen_count(self):
        return self._queen_count

    def print_board(self):
        for row in self._board:
            for col in row:
                if (col == CONST_CODE_QUEEN):
                    print ('Q', end=" ")
                else:
                    print('_', end=" ")
            print()

    # insert a queen (1) into a board at a given location, from 1 to 8 inclusively
    def insert_queen(self, row, col):
        # if location outside of board, return false
        if row < 1 > col or row > 8 < col:
            return False
        # if queen cannot be placed in given location, return false
        if self._board[row][col] != CONST_CODE_EMPTY:
            return False
        self._board[row][col] = CONST_CODE_QUEEN
        self._queen_count += 1

        # filling blocked positions with CONST_CODE_BLOCKED
        for i in range(size):
            # set recentlyInsertedRow of newest queen to be blocked if empty
            if self._board[row][i] == CONST_CODE_EMPTY:
                self._board[col][i] = CONST_CODE_BLOCKED;
            # set column of newest queen to be blocked if empty
            if self._board[i][col] == CONST_CODE_EMPTY:
                self._board[i][row] = CONST_CODE_BLOCKED;

            # do diagonal from piece to bottom right
            blockedRow = row + i
            blockedCol = col + i
            if blockedRow < size and blockedCol < size and self._board[blockedRow][blockedCol] == CONST_CODE_EMPTY:
                self._board[blockedRow][blockedCol] = CONST_CODE_BLOCKED;

            # do diagonal from piece to top left
            blockedRow = row - i
            blockedCol = col - i
            if blockedRow >= 0 and blockedCol >= 0 and self._board[blockedRow][blockedCol] == CONST_CODE_EMPTY:
                self._board[blockedRow][blockedCol] = CONST_CODE_BLOCKED;

            # do diagonal from piece to top right
            blockedRow = row - i
            blockedCol = col + i
            if blockedRow >= 0 and blockedCol < size and self._board[blockedRow][blockedCol] == CONST_CODE_EMPTY:
                self._board[blockedRow][blockedCol] = CONST_CODE_BLOCKED;

            # do diagonal from piece to bottom left
            blockedRow = row + i
            blockedCol = col - i
            if blockedRow < size and blockedCol >= 0 and self._board[blockedRow][blockedCol] == CONST_CODE_EMPTY:
                self._board[blockedRow][blockedCol] = CONST_CODE_BLOCKED
        return True

size = 8
starting_board = Board(size)
starting_board.insert_queen(1,1)
starting_board.print_board()