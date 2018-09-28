import copy

# these codes indicate the status of a position in the board
CONST_CODE_EMPTY = 0
CONST_CODE_BLOCKED = -1
CONST_CODE_QUEEN = 1
CONST_SOLUTION_PIECE_COUNT = 8

class Board:
    def __init__(self, size: int):
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

    def print_board_debug(self):
        for row in self._board:
            for col in row:
                if (col == CONST_CODE_QUEEN):
                    print ('Q', end=" ")
                elif col == CONST_CODE_BLOCKED:
                    print ('X ', end="")
                else:
                    print('_', end=" ")
            print()

    # insert a queen (1) into a board at a given location
    def insert_queen(self, row: int, col: int) -> bool:
        # if location outside of board, return false
        if row < 0 or col < 0 or row >= self._size or col >= self._size:
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
                self._board[row][i] = CONST_CODE_BLOCKED;
            # set column of newest queen to be blocked if empty
            if self._board[i][col] == CONST_CODE_EMPTY:
                self._board[i][col] = CONST_CODE_BLOCKED;

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

def depth_first_search(board: Board):
    for i in range(size):
        child = copy.deepcopy(board)
        piece_inserted = child.insert_queen(0, i)
        if child.get_queen_count() >= CONST_SOLUTION_PIECE_COUNT:
            solutions.append(child)
            return
        if piece_inserted:
            depth_first_search(child)


size = 8
starting_board = Board(size)
starting_board.insert_queen(4,4)
starting_board.print_board_debug()
solutions = list()
depth_first_search(starting_board)