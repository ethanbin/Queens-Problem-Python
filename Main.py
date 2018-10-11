import copy
from tkinter import *

# these codes indicate the status of a position in the board
CONST_CODE_EMPTY = 0
CONST_CODE_BLOCKED = -1
CONST_CODE_QUEEN = 1
CONST_SOLUTION_PIECE_COUNT = 8


class Board:
    solutions = list()
    def __init__(self, size: int):
        self._size = size
        self._queen_count = 0
        self._board  = [[0 for x in range(size)] for y in range(size)]
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
        for i in range(self._size):
            # set recentlyInsertedRow of newest queen to be blocked if empty
            if self._board[row][i] == CONST_CODE_EMPTY:
                self._board[row][i] = CONST_CODE_BLOCKED;
            # set column of newest queen to be blocked if empty
            if self._board[i][col] == CONST_CODE_EMPTY:
                self._board[i][col] = CONST_CODE_BLOCKED;

            # do diagonal from piece to bottom right
            blockedRow = row + i
            blockedCol = col + i
            if blockedRow < self._size and blockedCol < self._size and self._board[blockedRow][blockedCol] == CONST_CODE_EMPTY:
                self._board[blockedRow][blockedCol] = CONST_CODE_BLOCKED;

            # do diagonal from piece to top left
            blockedRow = row - i
            blockedCol = col - i
            if blockedRow >= 0 and blockedCol >= 0 and self._board[blockedRow][blockedCol] == CONST_CODE_EMPTY:
                self._board[blockedRow][blockedCol] = CONST_CODE_BLOCKED;

            # do diagonal from piece to top right
            blockedRow = row - i
            blockedCol = col + i
            if blockedRow >= 0 and blockedCol < self._size and self._board[blockedRow][blockedCol] == CONST_CODE_EMPTY:
                self._board[blockedRow][blockedCol] = CONST_CODE_BLOCKED;

            # do diagonal from piece to bottom left
            blockedRow = row + i
            blockedCol = col - i
            if blockedRow < self._size and blockedCol >= 0 and self._board[blockedRow][blockedCol] == CONST_CODE_EMPTY:
                self._board[blockedRow][blockedCol] = CONST_CODE_BLOCKED
        return True


def depth_first_search(board: Board, current_row:int):
    for i in range(board._size):
        child = copy.deepcopy(board)
        piece_inserted = child.insert_queen(i, current_row)
        # if child has 8 pieces, it is a solution and will have no more children,
        # so add to list of solutions and exit this recursive call
        if child.get_queen_count() >= CONST_SOLUTION_PIECE_COUNT:
            Board.solutions.append(child)
            return
        # if child had a piece inserted but is not yet a solution, traverse down this child
        if piece_inserted:
            depth_first_search(child, current_row+1)


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        quitButton = Button(self, text="Quit",command=self.client_exit)

        # placing the button on my window
        quitButton.place(x=0, y=0)

    def client_exit(self):
        exit()

def main():
    root = Tk()
    root.geometry("300x300")
    app = Window(root)
    root.mainloop()

    size = 8
    starting_board = Board(size)
    depth_first_search(starting_board, 0)
    for b in Board.solutions:
        b.print_board()
    print(len(Board.solutions))

if __name__ == '__main__':
    main()